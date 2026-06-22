import os
import sys

# Anchor every asset path to the application root, not the process CWD, so the
# app works regardless of where it is launched from and inside a frozen build.
if getattr(sys, "frozen", False):
    # PyInstaller extracts bundled data to sys._MEIPASS (see main.spec datas).
    base_directory = getattr(sys, "_MEIPASS", os.path.dirname(sys.executable))
else:
    base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

static_dir = os.path.join(base_directory, "static")
csv_dir = os.path.join(static_dir, "csv")
audio_dir = os.path.join(static_dir, "audio")
image_dir = os.path.join(static_dir, "image")

font_dir = os.path.join(static_dir, "font", "Noto_Sans_TC", "static", "NotoSansTC-Black.ttf")
user_dir = os.path.join(csv_dir, "user.csv")
history_dir = os.path.join(csv_dir, "history.csv")
exam_dir = os.path.join(csv_dir, "exam.csv")
volume_icon = os.path.join(image_dir, "volume.png")
keyboard_dir = os.path.join(csv_dir, "keyboard_layout")

metadata_dir = os.path.join(static_dir, "metadata", "default.json")
