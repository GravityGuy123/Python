import os
import subprocess

# ===============================
# 🔧 STEP 1: Paste your YouTube video URL below
# ===============================
video_url = "https://www.youtube.com/watch?v=kffacxfA7G4"  # ← Replace with your YouTube URL

# ===============================
# ⚙️ STEP 2: Settings
# ===============================
subtitle_lang = "en"     # Change 'en' to another language code (e.g., 'fr', 'es', 'de')
output_folder = "downloads"  # Folder to save the video and subtitles
ffmpeg_path = r"C:\Users\HP\AppData\Local\Microsoft\WinGet\Links"  # ✅ FFmpeg path added

# ===============================
# 🧠 STEP 3: Prepare Command
# ===============================
os.makedirs(output_folder, exist_ok=True)

command = [
    "yt-dlp",
    "--ffmpeg-location", ffmpeg_path,      # ✅ Use FFmpeg from this path
    "-f", "bestvideo[height<=480]+bestaudio/best[height<=480]/best",  # ✅ Prefer 480p, else nearest
    "--merge-output-format", "mp4",        # ✅ Merge into playable MP4
    "--write-auto-subs",                   # Get auto-generated subtitles
    "--sub-lang", subtitle_lang,           # Subtitle language
    "--convert-subs", "srt",               # Convert to .srt format
    "-o", f"{output_folder}/%(title)s.%(ext)s",  # Output format and name
    video_url
]

# ===============================
# 🚀 STEP 4: Run
# ===============================
try:
    subprocess.run(command, check=True)
    print(f"\n✅ Download completed successfully! Check the '{output_folder}' folder.")
except subprocess.CalledProcessError:
    print("\n❌ Error: Unable to download the video. Check the video URL or yt-dlp setup.")