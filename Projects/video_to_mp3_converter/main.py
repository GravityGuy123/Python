from moviepy import VideoFileClip
import os

def video_to_mp3(video_path, mp3_name=None):
    """
    Converts a given video file to MP3 format.
    
    Parameters:
        video_path (str): Full path or filename of the video.
        mp3_name (str): Desired MP3 output filename (optional).
    """

    # Extract folder where the video is located
    folder = os.path.dirname(video_path) or os.getcwd()

    # If user didn’t specify MP3 name, use video name automatically
    if not mp3_name:
        mp3_name = os.path.splitext(os.path.basename(video_path))[0] + ".mp3"

    # Join folder and MP3 name to create full output path
    output_path = os.path.join(folder, mp3_name)

    try:
        print(f"🎬 Converting '{video_path}' to MP3...\n")

        # Load video file
        video = VideoFileClip(video_path)

        # Extract and write audio as MP3
        video.audio.write_audiofile(output_path)

        print(f"\n✅ Conversion successful! MP3 saved as:\n{output_path}")

    except Exception as e:
        print(f"\n❌ Error: {e}")

    finally:
        # Release system resources
        if 'video' in locals():
            video.close()


# -------------------- 🔽 INSTRUCTIONS BELOW 🔽 --------------------

# STEP 1️⃣: Enter your VIDEO file name or path between the quotes below
# Example: "myvideo.mp4" if it’s in the same folder as this script
# Or: "C:/Users/Simon/Videos/myvideo.mp4" for a full path
video_file = "example.mp4"   # 👈 ENTER YOUR VIDEO NAME OR PATH HERE

# STEP 2️⃣: (Optional) Enter your desired MP3 output filename
# Example: "mysong.mp3"
# If you leave it empty (""), it will automatically use the video name.
mp3_file_name = "mysong.mp3"  # 👈 ENTER YOUR NEW MP3 NAME HERE

# STEP 3️⃣: Run the converter
video_to_mp3(video_file, mp3_file_name)