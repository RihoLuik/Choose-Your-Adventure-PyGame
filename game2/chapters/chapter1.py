import pygame
import subprocess
import time
from game2.choices import save_choice, determine_next_chapter
from game2.dialogue import display_dialogue, get_choice
from game2.save import save_progress
from settings import apply_settings

# Initialize Pygame
pygame.init()
screen, settings = apply_settings()
pygame.display.set_caption('Game2 - Chapter 1')

# Display intro dialogue
display_dialogue(screen, "Unknown", "A Job well done, young one. Go home now... you need to rest. I'll contact you when I got something.")
time.sleep(5)
display_dialogue(screen, "...", "...*sigh*, I should get home and rest up")
time.sleep(5)
display_dialogue(screen, "System", "*you notice something in the corner of your eye, something on the ground.*")
time.sleep(5)
display_dialogue(screen, "...", "What's this...? A phone of sorts...?")
time.sleep(5)
display_dialogue(screen, "System", "You look at the phone a little closer. What do you do?",
                 ["Pick Up the Phone", "Leave it where it is"])

# Get player's choice
choice = get_choice()

if choice == 0:
    save_choice("good")
    display_dialogue(screen, "System", "You picked up the phone.")
    time.sleep(5)
    display_dialogue(screen, "...", "The phone looks good, surprised it's not broken.")
    time.sleep(5)
    display_dialogue(screen, "...", "I'll take it back home and see what I can learn about it.")
    time.sleep(5)

elif choice == 1:
    save_choice("bad")
    display_dialogue(screen, "System", "You left the phone where it was.")
    time.sleep(5)
    display_dialogue(screen, "...", "Eh, whatever, probably not important anyway.")
    time.sleep(5)

# Determine next chapter dynamically
next_chapter = determine_next_chapter()
display_dialogue(screen, "System", f"Loading next chapter...")
time.sleep(5)

print("Chapter 1 completed! Saving progress...")
save_progress(f"{next_chapter}") # Save progress before moving on

# Load the next chapter
pygame.quit()
subprocess.run(["python", f"game2/chapters/{next_chapter}"])