from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

from PIL import Image, ImageOps, features


@dataclass(frozen=True)
class ConvertOptions:
    out_format: str
    out_dir: Optional[Path]
    suffix: str
    overwrite: bool
    keep_icc: bool
    keep_exif: bool
    background_rgb: tuple[int, int, int]
    ico_sizes: tuple[tuple[int, int], ...]
    ico_crop_square: bool
    webp_quality: int
    webp_lossless: bool
    avif_quality: int


# -----------------------------
# Format support helpers
# -----------------------------

def normalize_format(fmt: str) -> str:
    f = fmt.strip().upper()
    return "JPEG" if f == "JPG" else f


def ext_for_format(fmt: str) -> str:
    fmt = normalize_format(fmt)
    mapping = {
        "JPEG": ".jpg",
        "PNG": ".png",
        "WEBP": ".webp",
        "TIFF": ".tiff",
        "BMP": ".bmp",
        "GIF": ".gif",
        "ICO": ".ico",
        "PDF": ".pdf",
        "AVIF": ".avif",
    }
    return mapping.get(fmt, f".{fmt.lower()}")


def supported_output_formats() -> dict[str, bool]:
    # Pillow registers core formats; availability depends on build/plugins.
    # This reports "likely supported" by checking feature flags where applicable.
    # Note: even if a feature says False, some installs may still load via plugin.
    candidates = [
        "JPEG",
        "PNG",
        "WEBP",
        "TIFF",
        "BMP",
        "GIF",
        "ICO",
        "PDF",
        "AVIF",
        "HEIF",
    ]

    def has_feature(name: str) -> bool:
        try:
            return bool(features.check(name))
        except Exception:
            return False

    result: dict[str, bool] = {}
    for fmt in candidates:
        if fmt == "WEBP":
            result[fmt] = has_feature("webp")
        elif fmt == "AVIF":
            # Pillow uses "avif" feature when built with it / plugin.
            result[fmt] = has_feature("avif")
        elif fmt == "HEIF":
            result[fmt] = has_feature("heif")
        else:
            # Common formats usually supported
            result[fmt] = True
    return result


# -----------------------------
# Image processing helpers
# -----------------------------

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

    # Avoid collisions: name-1, name-2...
    i = 1
    while True:
        candidate = folder / f"{base}{suffix}-{i}{ext}"
        if not candidate.exists():
            return candidate
        i += 1


def fix_orientation(img: Image.Image) -> Image.Image:
    # Fixes images that appear rotated due to EXIF orientation flag
    try:
        return ImageOps.exif_transpose(img)
    except Exception:
        return img


def flatten_alpha(img: Image.Image, bg: tuple[int, int, int]) -> Image.Image:
    # For formats that don't support alpha (JPEG, etc.)
    if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
        base = Image.new("RGB", img.size, bg)
        rgba = img.convert("RGBA")
        base.paste(rgba, mask=rgba.split()[-1])
        return base
    if img.mode != "RGB":
        return img.convert("RGB")
    return img


def crop_center_square(img: Image.Image) -> Image.Image:
    w, h = img.size
    size = min(w, h)
    left = (w - size) // 2
    top = (h - size) // 2
    return img.crop((left, top, left + size, top + size))


# -----------------------------
# Core conversion logic
# -----------------------------

def convert_one(input_path: Path, opts: ConvertOptions) -> Path:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    out_format = normalize_format(opts.out_format)
    out_ext = ext_for_format(out_format)

    with Image.open(input_path) as img:
        img = fix_orientation(img)

        icc_profile = img.info.get("icc_profile") if opts.keep_icc else None
        exif = img.info.get("exif") if opts.keep_exif else None

        # ICO requires special handling: RGBA + square + multi-size
        if out_format == "ICO":
            ico_img = img.convert("RGBA")
            if opts.ico_crop_square:
                ico_img = crop_center_square(ico_img)
            # Use a high base size; Pillow will downsample to sizes list
            ico_img = ico_img.resize((256, 256), Image.LANCZOS)

            out_path = ensure_out_path(input_path, opts.out_dir, opts.suffix, out_ext, opts.overwrite)
            ico_img.save(
                out_path,
                format="ICO",
                sizes=list(opts.ico_sizes),
            )
            return out_path

        # Decide if target supports alpha
        supports_alpha = out_format in ("PNG", "WEBP", "TIFF", "GIF")
        # PDF and BMP are RGB-only in typical use here
        if not supports_alpha:
            img = flatten_alpha(img, opts.background_rgb)

        out_path = ensure_out_path(input_path, opts.out_dir, opts.suffix, out_ext, opts.overwrite)

        save_kwargs: dict[str, object] = {}

        if icc_profile is not None:
            save_kwargs["icc_profile"] = icc_profile
        if exif is not None:
            save_kwargs["exif"] = exif

        if out_format == "JPEG":
            save_kwargs["quality"] = 92
            save_kwargs["optimize"] = True
            save_kwargs["progressive"] = True
            img.save(out_path, format="JPEG", **save_kwargs)
        elif out_format == "WEBP":
            save_kwargs["quality"] = int(opts.webp_quality)
            save_kwargs["lossless"] = bool(opts.webp_lossless)
            save_kwargs["method"] = 6
            img.save(out_path, format="WEBP", **save_kwargs)
        elif out_format == "AVIF":
            # Works only if your Pillow build/plugin supports it
            save_kwargs["quality"] = int(opts.avif_quality)
            img.save(out_path, format="AVIF", **save_kwargs)
        else:
            img.save(out_path, format=out_format, **save_kwargs)

        return out_path


def convert_many(inputs: Iterable[Path], opts: ConvertOptions) -> int:
    ok = 0
    for p in inputs:
        try:
            out = convert_one(p, opts)
            print(f"✅ {p.name} → {out.name} ({normalize_format(opts.out_format)})")
            ok += 1
        except Exception as e:
            print(f"❌ {p}: {e}")
    return ok


# -----------------------------
# CLI
# -----------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="image_format_converter.py",
        description="Production-grade image format converter (single or batch).",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list-formats", help="List formats you can convert to on this machine.")
    p_list.add_argument("--verbose", action="store_true", help="Print notes about plugin-based formats.")

    p_convert = sub.add_parser("convert", help="Convert one or more images to a target format.")
    p_convert.add_argument("inputs", nargs="+", help="Input image file(s).")
    p_convert.add_argument(
        "--to",
        required=True,
        help="Target format (e.g. JPEG, PNG, WEBP, ICO, PDF, TIFF, BMP, GIF, AVIF).",
    )
    p_convert.add_argument("--out-dir", default=None, help="Output directory (default: same folder).")
    p_convert.add_argument("--suffix", default="_converted", help="Filename suffix (default: _converted).")
    p_convert.add_argument("--overwrite", action="store_true", help="Overwrite if output exists.")
    p_convert.add_argument("--no-icc", action="store_true", help="Do not preserve ICC profile.")
    p_convert.add_argument("--no-exif", action="store_true", help="Do not preserve EXIF.")
    p_convert.add_argument(
        "--background",
        type=parse_rgb,
        default=(255, 255, 255),
        help="Flatten alpha to this RGB background when needed (default: 255,255,255).",
    )

    # ICO
    p_convert.add_argument(
        "--ico-sizes",
        default="16,16;32,32;48,48;64,64;128,128;256,256",
        help="ICO sizes as 'w,h;w,h;...' (default includes 16..256).",
    )
    p_convert.add_argument(
        "--ico-no-crop",
        action="store_true",
        help="Do not crop to square for ICO (default is crop).",
    )

    # WEBP
    p_convert.add_argument("--webp-quality", type=int, default=82, help="WEBP quality (0-100).")
    p_convert.add_argument("--webp-lossless", action="store_true", help="Use WEBP lossless compression.")

    # AVIF
    p_convert.add_argument("--avif-quality", type=int, default=50, help="AVIF quality (0-100).")

    return parser


def parse_ico_sizes(spec: str) -> tuple[tuple[int, int], ...]:
    # spec: "16,16;32,32;..."
    parts = [x.strip() for x in spec.split(";") if x.strip()]
    sizes: list[tuple[int, int]] = []
    for item in parts:
        wh = [v.strip() for v in item.split(",")]
        if len(wh) != 2:
            raise ValueError("Invalid --ico-sizes. Use 'w,h;w,h;...'")
        w = int(wh[0])
        h = int(wh[1])
        if w <= 0 or h <= 0:
            raise ValueError("ICO sizes must be positive.")
        sizes.append((w, h))
    if not sizes:
        raise ValueError("ICO sizes list is empty.")
    return tuple(sizes)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.cmd == "list-formats":
        fmts = supported_output_formats()
        print("Supported output formats (based on your Pillow build):")
        for k in ["JPEG", "PNG", "WEBP", "AVIF", "TIFF", "BMP", "GIF", "ICO", "PDF", "HEIF"]:
            v = fmts.get(k, False)
            print(f" - {k}: {'✅' if v else '❌'}")
        if args.verbose:
            print("\nNotes:")
            print(" - WEBP/AVIF/HEIF availability depends on your Pillow build/plugins.")
            print(" - If AVIF shows ❌, you can still convert to WEBP/JPEG/PNG reliably.")
        return

    if args.cmd == "convert":
        out_format = normalize_format(args.to)

        try:
            ico_sizes = parse_ico_sizes(args.ico_sizes)
        except Exception as e:
            raise SystemExit(f"Invalid --ico-sizes: {e}")

        opts = ConvertOptions(
            out_format=out_format,
            out_dir=Path(args.out_dir) if args.out_dir else None,
            suffix=str(args.suffix),
            overwrite=bool(args.overwrite),
            keep_icc=not bool(args.no_icc),
            keep_exif=not bool(args.no_exif),
            background_rgb=tuple(args.background),
            ico_sizes=ico_sizes,
            ico_crop_square=not bool(args.ico_no_crop),
            webp_quality=int(args.webp_quality),
            webp_lossless=bool(args.webp_lossless),
            avif_quality=int(args.avif_quality),
        )

        inputs = [Path(p) for p in args.inputs]
        ok = convert_many(inputs, opts)
        print(f"\nDone. Converted {ok}/{len(inputs)} file(s).")


if __name__ == "__main__":
    main()



# # How to use (converter)
# python image_format_converter.py list-formats --verbose
# python image_format_converter.py convert photo.png --to WEBP
# python image_format_converter.py convert favicon.png --to ICO
# python image_format_converter.py convert a.png b.jpg c.webp --to PNG --out-dir ./out
# python image_format_converter.py convert transparent.png --to JPEG --background 255,255,255