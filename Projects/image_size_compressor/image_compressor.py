from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

from PIL import Image, ImageOps


@dataclass(frozen=True)
class CompressOptions:
    out_dir: Optional[Path]
    suffix: str
    overwrite: bool
    keep_icc: bool
    keep_exif: bool
    max_width: int
    max_height: int
    out_format: Optional[str]  # None = keep original when possible
    quality: int
    target_kb: Optional[int]
    min_quality: int
    optimize: bool
    progressive: bool
    background_rgb: tuple[int, int, int]
    webp_lossless: bool
    unicode_output: bool


def safe_print(text: str) -> None:
    """
    Print without crashing on Windows terminals that default to cp1252.
    - Tries normal print first.
    - If UnicodeEncodeError happens, prints an ASCII-safe version.
    """
    try:
        print(text)
        return
    except UnicodeEncodeError:
        # Fallback: replace non-encodable chars with '?'
        encoded = text.encode(sys.stdout.encoding or "utf-8", errors="replace")
        sys.stdout.buffer.write(encoded + os.linesep.encode(sys.stdout.encoding or "utf-8", errors="replace"))
        sys.stdout.flush()


def normalize_format(fmt: str) -> str:
    f = fmt.strip().upper()
    return "JPEG" if f == "JPG" else f


def parse_rgb(s: str) -> tuple[int, int, int]:
    parts = [p.strip() for p in s.split(",")]
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("background must be 'R,G,B' e.g. 255,255,255")
    try:
        r, g, b = (int(parts[0]), int(parts[1]), int(parts[2]))
    except ValueError:
        raise argparse.ArgumentTypeError("background values must be integers")
    for v, n in ((r, "R"), (g, "G"), (b, "B")):
        if v < 0 or v > 255:
            raise argparse.ArgumentTypeError(f"{n} must be 0..255")
    return (r, g, b)


def ensure_out_path(
    input_path: Path,
    out_dir: Optional[Path],
    suffix: str,
    ext: str,
    overwrite: bool,
) -> Path:
    folder = out_dir if out_dir else input_path.parent
    folder.mkdir(parents=True, exist_ok=True)

    base = input_path.stem
    out_path = folder / f"{base}{suffix}{ext}"

    if overwrite:
        return out_path

    if not out_path.exists():
        return out_path

    i = 1
    while True:
        candidate = folder / f"{base}{suffix}-{i}{ext}"
        if not candidate.exists():
            return candidate
        i += 1


def fix_orientation(img: Image.Image) -> Image.Image:
    try:
        return ImageOps.exif_transpose(img)
    except Exception:
        return img


def has_alpha(img: Image.Image) -> bool:
    if img.mode in ("RGBA", "LA"):
        return True
    if img.mode == "P" and "transparency" in img.info:
        return True
    return False


def flatten_alpha(img: Image.Image, bg: tuple[int, int, int]) -> Image.Image:
    if not has_alpha(img):
        return img.convert("RGB") if img.mode != "RGB" else img
    base = Image.new("RGB", img.size, bg)
    rgba = img.convert("RGBA")
    base.paste(rgba, mask=rgba.split()[-1])
    return base


def resize_if_needed(img: Image.Image, max_w: int, max_h: int) -> Image.Image:
    if max_w <= 0 or max_h <= 0:
        return img
    w, h = img.size
    if w <= max_w and h <= max_h:
        return img
    copy = img.copy()
    copy.thumbnail((max_w, max_h), Image.LANCZOS)
    return copy


def save_image(
    img: Image.Image,
    out_path: Path,
    out_format: str,
    quality: int,
    optimize: bool,
    progressive: bool,
    keep_icc: bool,
    keep_exif: bool,
    icc_profile: Optional[bytes],
    exif: Optional[bytes],
    webp_lossless: bool,
) -> None:
    fmt = normalize_format(out_format)
    save_kwargs: dict[str, object] = {}

    if keep_icc and icc_profile is not None:
        save_kwargs["icc_profile"] = icc_profile
    if keep_exif and exif is not None:
        save_kwargs["exif"] = exif

    if fmt == "JPEG":
        save_kwargs["quality"] = int(quality)
        save_kwargs["optimize"] = bool(optimize)
        save_kwargs["progressive"] = bool(progressive)
        img.save(out_path, format="JPEG", **save_kwargs)
        return

    if fmt == "PNG":
        # PNG ignores "quality"; optimize helps
        save_kwargs["optimize"] = bool(optimize)
        img.save(out_path, format="PNG", **save_kwargs)
        return

    if fmt == "WEBP":
        save_kwargs["quality"] = int(quality)
        save_kwargs["lossless"] = bool(webp_lossless)
        save_kwargs["method"] = 6
        img.save(out_path, format="WEBP", **save_kwargs)
        return

    # Fallback: try saving in requested format
    img.save(out_path, format=fmt, **save_kwargs)


def compress_one(input_path: Path, opts: CompressOptions) -> Path:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with Image.open(input_path) as img:
        img = fix_orientation(img)

        icc_profile = img.info.get("icc_profile")
        exif = img.info.get("exif")

        img = resize_if_needed(img, opts.max_width, opts.max_height)

        # Decide output format
        chosen_format: str
        if opts.out_format:
            chosen_format = normalize_format(opts.out_format)
        else:
            # Keep original format where it makes sense
            chosen_format = normalize_format(img.format or "JPEG")

        # Ensure extension matches format
        ext_map = {"JPEG": ".jpg", "PNG": ".png", "WEBP": ".webp"}
        ext = ext_map.get(chosen_format, f".{chosen_format.lower()}")

        # Alpha rules: JPEG can't keep alpha
        if chosen_format == "JPEG":
            img_to_save = flatten_alpha(img, opts.background_rgb)
        else:
            img_to_save = img

        out_path = ensure_out_path(input_path, opts.out_dir, opts.suffix, ext, opts.overwrite)

        # If target_kb is provided, try multiple qualities
        if opts.target_kb is not None and chosen_format in ("JPEG", "WEBP"):
            target_bytes = int(opts.target_kb) * 1024
            q = int(opts.quality)
            best_path = out_path

            while True:
                save_image(
                    img_to_save,
                    best_path,
                    chosen_format,
                    q,
                    opts.optimize,
                    opts.progressive,
                    opts.keep_icc,
                    opts.keep_exif,
                    icc_profile,
                    exif,
                    opts.webp_lossless,
                )
                size_bytes = best_path.stat().st_size
                if size_bytes <= target_bytes or q <= opts.min_quality:
                    break
                q = max(opts.min_quality, q - 6)
            return best_path

        # Simple one-pass save
        save_image(
            img_to_save,
            out_path,
            chosen_format,
            opts.quality,
            opts.optimize,
            opts.progressive,
            opts.keep_icc,
            opts.keep_exif,
            icc_profile,
            exif,
            opts.webp_lossless,
        )
        return out_path


def compress_many(inputs: Iterable[Path], opts: CompressOptions) -> int:
    ok = 0
    for p in inputs:
        try:
            before = p.stat().st_size
            out = compress_one(p, opts)
            after = out.stat().st_size
            saved = 0.0 if before == 0 else (1.0 - (after / before)) * 100.0

            if opts.unicode_output:
                msg = f"✅ {p.name} → {out.name} | -{saved:.1f}%"
            else:
                msg = f"[OK] {p.name} -> {out.name} | -{saved:.1f}%"

            safe_print(msg)
            ok += 1
        except Exception as e:
            if opts.unicode_output:
                safe_print(f"❌ {p}: {e}")
            else:
                safe_print(f"[ERR] {p}: {e}")
    return ok


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="image_compressor.py",
        description="Production-grade image compressor (single or batch).",
    )
    parser.add_argument("inputs", nargs="+", help="Input image file(s).")
    parser.add_argument("--out-dir", default=None, help="Output directory (default: same folder).")
    parser.add_argument("--suffix", default="_compressed", help="Filename suffix (default: _compressed).")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite if output exists.")
    parser.add_argument("--no-icc", action="store_true", help="Do not preserve ICC profile.")
    parser.add_argument("--no-exif", action="store_true", help="Do not preserve EXIF.")
    parser.add_argument("--max-width", type=int, default=1920, help="Max width (default 1920).")
    parser.add_argument("--max-height", type=int, default=1080, help="Max height (default 1080).")
    parser.add_argument(
        "--format",
        default=None,
        help="Force output format (JPEG, PNG, WEBP). Default: keep original when possible.",
    )
    parser.add_argument("--quality", type=int, default=82, help="Quality 1-100 (default 82).")
    parser.add_argument(
        "--target-kb",
        type=int,
        default=None,
        help="Target size in KB (JPEG/WEBP only). Auto reduces quality until under size.",
    )
    parser.add_argument("--min-quality", type=int, default=40, help="Minimum auto quality (default 40).")
    parser.add_argument("--no-optimize", action="store_true", help="Disable optimize=True.")
    parser.add_argument("--no-progressive", action="store_true", help="Disable progressive JPEG.")
    parser.add_argument(
        "--background",
        type=parse_rgb,
        default=(255, 255, 255),
        help="Background RGB for flattening alpha when saving JPEG (default 255,255,255).",
    )
    parser.add_argument("--webp-lossless", action="store_true", help="Use WEBP lossless compression.")
    parser.add_argument(
        "--unicode",
        action="store_true",
        help="Use unicode symbols in output (✅ ❌ →). Only enable if your terminal supports UTF-8.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    q = int(args.quality)
    if q < 1 or q > 100:
        raise SystemExit("--quality must be 1..100")

    min_q = int(args.min_quality)
    if min_q < 1 or min_q > 100:
        raise SystemExit("--min-quality must be 1..100")

    if args.target_kb is not None and args.target_kb <= 0:
        raise SystemExit("--target-kb must be > 0")

    out_format = normalize_format(args.format) if args.format else None
    if out_format and out_format not in ("JPEG", "PNG", "WEBP"):
        raise SystemExit("--format must be one of: JPEG, PNG, WEBP")

    opts = CompressOptions(
        out_dir=Path(args.out_dir) if args.out_dir else None,
        suffix=str(args.suffix),
        overwrite=bool(args.overwrite),
        keep_icc=not bool(args.no_icc),
        keep_exif=not bool(args.no_exif),
        max_width=int(args.max_width),
        max_height=int(args.max_height),
        out_format=out_format,
        quality=q,
        target_kb=int(args.target_kb) if args.target_kb is not None else None,
        min_quality=min_q,
        optimize=not bool(args.no_optimize),
        progressive=not bool(args.no_progressive),
        background_rgb=tuple(args.background),
        webp_lossless=bool(args.webp_lossless),
        unicode_output=bool(args.unicode),
    )

    inputs = [Path(p) for p in args.inputs]
    ok = compress_many(inputs, opts)
    safe_print(f"\nDone. Compressed {ok}/{len(inputs)} file(s).")


if __name__ == "__main__":
    main()


# # How to use (compressor)
# # 1. Best Command
# python image_compressor.py image.jpg --format WEBP --quality 82
# python image_compressor.py og.png --format JPG --quality 82
#
# # 2. Compress all in jfif format and convert to webp
# python image_compressor.py *.jfif --format WEBP --quality 82
#
# # 3. Simple compress, keep format when possible
# python image_compressor.py photo.png
#
# # 4. Force JPEG output (best for photos)
# python image_compressor.py big.png --format JPEG --quality 82
#
# # 5. Target file size (auto reduces quality)
# python image_compressor.py photo.jpg --format JPEG --target-kb 250 --quality 90 --min-quality 40
#
# # 6. Resize + compress
# python image_compressor.py photo.jpg --max-width 1600 --max-height 900 --quality 80
#
# # 7. Batch
# python image_compressor.py ./images/a.jpg ./images/b.png --out-dir ./out --format WEBP --quality 82