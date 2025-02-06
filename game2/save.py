import json
import subprocess
import sys

SAVE_FILE = "game2/save_data.json"

# Load the saved game progress
def load_save():
    try:
        with open(SAVE_FILE, "r") as file:
            save_data = json.load(file)
            last_chapter = save_data["last_chapter", "chapter1.py"] # Default to chapter1 if no save
    except (FileNotFoundError, json.JSONDecodeError):
        last_chapter = "chapter1.py" # Start fresh if save is missing

    print(f"Loading {last_chapter}...")
    subprocess.run(["python", f"game2/chapters/{last_chapter}"])
    sys.exit()

# Save current progress (called from chapter scripts)
def save_progress(chapter_name):
    save_data = {"last_chapter": chapter_name}
    with open(SAVE_FILE, "w") as file:
        json.dump(save_data, file)

if __name__ == "__main__":
    load_save()