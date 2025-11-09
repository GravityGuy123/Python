from PIL import Image
import os

def convert_image(input_path, output_format="JPEG"):
    """
    Convert an image from one format to another.

    Parameters:
        input_path (str): The path or filename of the image to convert.
        output_format (str): The target format. Must be one of the supported formats below.
    """
    try:
        # Open the image
        image = Image.open(input_path)

        # Convert to RGB if the image has transparency (e.g. PNG)
        # Some formats (like JPEG) do not support transparency.
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        # Split filename and extension
        file_root, _ = os.path.splitext(input_path)

        # Set output file name and new extension
        output_ext = output_format.lower()
        output_path = f"{file_root}_converted.{output_ext}"

        # --- ✅ FIX: Handle ICO format properly ---
        if output_format.upper() == "ICO":
            # Reopen original to preserve transparency
            image = Image.open(input_path)
            if image.mode != "RGBA":
                image = image.convert("RGBA")
            image.save(output_path, format="ICO", sizes=[(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)])
        else:
            # Save image in the new format (default behavior)
            image.save(output_path, format=output_format)
        # --- ✅ END FIX ---

        print(f"✅ Conversion successful!")
        print(f"📁 Original file: {input_path}")
        print(f"📦 New file: {output_path}")
        print(f"🎨 Converted to format: {output_format}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    # 🖼️ INSTRUCTIONS:
    # 1️⃣ Place this script in the same folder as your image.
    # 2️⃣ Enter your image file name or path below.
    #    Examples:
    #    input_image = "my_photo.png"             # same folder
    #    input_image = "images/sample.webp"       # subfolder
    #    input_image = r"C:\Users\HP\Desktop\pic.jpg"  # full path
    input_image = "logo.png"  # ← Change this to your image name or path

    # 🎯 SUPPORTED OUTPUT FORMATS:
    # You can convert to any of these:
    #
    #  - "JPEG" → Joint Photographic Experts Group (good for photos)
    #  - "JPG"  → same as JPEG
    #  - "PNG"  → Portable Network Graphics (supports transparency)
    #  - "WEBP" → High compression, web-optimized, supports transparency
    #  - "ICO"  → Windows icon format (useful for app or favicon icons)
    #  - "BMP"  → Bitmap format (uncompressed, large size)
    #  - "TIFF" → Tagged Image File Format (used for printing/scanning)
    #  - "GIF"  → Graphics Interchange Format (supports simple animations)
    #
    # 👉 Just type one of the above as the format name below.
    target_format = "ICO"  # ← Change this to your desired format

    # 🚀 Run the conversion
    convert_image(input_image, output_format=target_format)