from PIL import Image
import os

def convert_image(input_path, output_format="JPEG"):
    """
    Convert an image from one format to another.

    Parameters:
        input_path (str): The path or filename of the image to convert.
        output_format (str): The target format.
    """
    try:
        image = Image.open(input_path)

        file_root, _ = os.path.splitext(input_path)
        output_ext = output_format.lower()
        output_path = f"{file_root}_converted.{output_ext}"

        # --- FIXED ICO HANDLING (WINDOWS SAFE) ---
        if output_format.upper() == "ICO":
            image = image.convert("RGBA")

            # Force square
            w, h = image.size
            size = min(w, h)
            left = (w - size) // 2
            top = (h - size) // 2
            image = image.crop((left, top, left + size, top + size))

            # Resize base image (Pillow will derive other sizes correctly)
            image = image.resize((256, 256), Image.LANCZOS)

            image.save(
                output_path,
                format="ICO",
                sizes=[(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)]
            )

        else:
            if image.mode in ("RGBA", "P"):
                image = image.convert("RGB")
            image.save(output_path, format=output_format)
        # --- END FIX ---

        print("✅ Conversion successful!")
        print(f"📁 Original file: {input_path}")
        print(f"📦 New file: {output_path}")
        print(f"🎨 Converted to format: {output_format}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    input_image = "favicon.jpg"   # Change if needed
    target_format = "ICO"      # Desired format
    convert_image(input_image, output_format=target_format)
