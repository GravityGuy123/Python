import os
import subprocess

# ===============================
# 🔧 STEP 1: Paste your YouTube video URL below
# ===============================
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # ← Replace with your YouTube URL

# ===============================
# ⚙️ STEP 2: Settings
# ===============================
subtitle_lang = "en"     # Change 'en' to another language code (e.g., 'fr', 'es', 'de')
output_folder = "subtitles"  # Folder to save the subtitle file
ffmpeg_path = r"C:\Users\HP\AppData\Local\Microsoft\WinGet\Links"  # ✅ FFmpeg path added

# ===============================
# 🧠 STEP 3: Prepare Command
# ===============================
os.makedirs(output_folder, exist_ok=True)

command = [
    "yt-dlp",
    "--ffmpeg-location", ffmpeg_path,  # ✅ Added FFmpeg path
    "--skip-download",                 # Don't download the video
    "--write-auto-subs",               # Get auto-generated subtitles
    "--sub-lang", subtitle_lang,       # Subtitle language
    "--convert-subs", "srt",           # Convert to .srt format
    "-o", f"{output_folder}/%(title)s.%(ext)s",  # Save name format
    video_url
]

# ===============================
# 🚀 STEP 4: Run
# ===============================
try:
    subprocess.run(command, check=True)
    print(f"\n✅ Subtitle downloaded successfully! Check the '{output_folder}' folder.")
except subprocess.CalledProcessError:
    print("\n❌ Error: Unable to download subtitles. Check the video URL or yt-dlp setup.")