from PIL import Image
import os
import json

def compress_image(input_path, output_path=None, quality=85, max_width=1920, max_height=1080, force_jpeg=True):
    """
    Compress an image while maintaining visual quality.
    Automatically reduces file size on repeated runs by lowering quality each time.
    """
    try:
        # Open image
        image = Image.open(input_path)

        # Convert to RGB if needed (for PNGs with transparency)
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        # Resize if too large
        image.thumbnail((max_width, max_height))

        # Change extension if forcing JPEG (better compression)
        file_root, file_ext = os.path.splitext(input_path)
        if not output_path:
            if force_jpeg:
                output_path = f"{file_root}_compressed.jpg"
            else:
                output_path = f"{file_root}_compressed{file_ext}"

        # Save compressed image
        image.save(output_path, format="JPEG" if force_jpeg else None, optimize=True, quality=quality)

        # Compare file sizes
        original_size = os.path.getsize(input_path) / 1024
        compressed_size = os.path.getsize(output_path) / 1024

        print(f"✅ Compressed successfully!")
        print(f"📁 Original: {original_size:.2f} KB")
        print(f"📦 Compressed: {compressed_size:.2f} KB")
        print(f"🔻 Reduced by: {100 - (compressed_size / original_size * 100):.1f}%")
        print(f"💾 Saved as: {output_path}")

        # Save the new (lower) quality value for the next run
        save_quality_setting(quality - 10 if quality > 20 else 20)

    except Exception as e:
        print(f"❌ Error: {e}")


def save_quality_setting(new_quality):
    """Save the next compression quality into a small JSON file."""
    with open("compression_settings.json", "w") as f:
        json.dump({"quality": new_quality}, f)
    print(f"⚙️ Next run will use quality={new_quality}")


def load_quality_setting(default=85):
    """
    Load the previously used compression quality from a JSON file.
    If no file exists (first run), start with the default quality value (85).
    """
    if os.path.exists("compression_settings.json"):
        try:
            with open("compression_settings.json", "r") as f:
                data = json.load(f)
            return data.get("quality", default)
        except:
            return default
    return default


if __name__ == "__main__":
    # 🖼️ Specify the image name or path here:
    input_image = "on_red_suit_sitting_on_white_staircase.png"  # ← Change this if needed

    # 🔄 HOW AUTO-REDUCTION WORKS:
    # 1️⃣ First time you run this script → uses quality=85
    # 2️⃣ It creates a file "compression_settings.json" to store the current quality value
    # 3️⃣ Each time you re-run it, the quality automatically drops by 10 (85 → 75 → 65 → etc.)
    # 4️⃣ It stops reducing below 20 to prevent extreme blur
    # 5️⃣ To reset back to 85, just delete the "compression_settings.json" file

    # 📉 Load the current (or last used) quality
    current_quality = load_quality_setting(default=85)

    # 🚀 Compress image
    compress_image(input_image, quality=current_quality, force_jpeg=True)