import pygame # should probably keep it, maybe dialogue and other stuff require it?
import time
from game1.save import save_progress

print("Chapter 1: The Beginning...")
time.sleep(3)

print("Chapter 1 completed! Saving progress...")
save_progress("chapter2.py") # Save progress before moving on

# Load the next chapter
import subprocess
subprocess.run(["python", "game1/chapters/chapter2.py"])