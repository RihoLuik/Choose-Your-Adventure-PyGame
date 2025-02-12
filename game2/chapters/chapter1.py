import pygame
import time
import json
import os
from game2.choices import save_choice, determine_next_chapter
from game2.dialogue import display_dialogue, get_choice
from game2.save import save_progress
from settings import apply_settings

CHOICES_FILE = "game2/choices.json"

# Clears choices.json when starting from Chapter 1
def reset_choices():
    empty_data = {"good": 0, "bad": 0}
    try:
        with open(CHOICES_FILE, "w") as file:
            json.dump(empty_data, file, indent=4)
        print("Choices have been reset!")
    except Exception as e:
        print(f"Error resetting choices: {e}")

# Runs Chapter 1 inside the Game2 window
def run_chapter(screen):
    settings = apply_settings()[1] # Get settings
    pygame.display.set_caption('Game2 - Chapter 1')

    print("Starting Chapter 1...")

    # Check if we are starting fresh
    if os.path.basename(__file__) == "chapter1.py":
        reset_choices()
    # Display intro dialogue
    display_dialogue(screen, "Unknown", "A Job well done, young one. Go home now... you need to rest. I'll contact you when I got something.")
    display_dialogue(screen, "...", "...*sigh*, I should get home and rest up")
    display_dialogue(screen, "System", "*you notice something in the corner of your eye, something on the ground.*")
    display_dialogue(screen, "...", "What's this...? A phone of sorts...?")
    display_dialogue(screen, "System", "You look at the phone and think... What do you do?", ["Pick Up the Phone", "Leave it where it is"])
    # Get player's choice
    choice = get_choice()

    if choice == 0:
        save_choice("good")
        display_dialogue(screen, "System", "You picked up the phone.")
        display_dialogue(screen, "...", "The phone looks good, surprised it's not damaged or broken.")
        display_dialogue(screen, "...", "I'll take it back home, see what I can learn about it.")

    elif choice == 1:
        save_choice("bad")
        display_dialogue(screen, "System", "You left the phone where it was.")
        display_dialogue(screen, "...", "No, doesn't matter, it's probably not important anyway.")

    # Determine next chapter dynamically
    next_chapter = determine_next_chapter()
    display_dialogue(screen, "System", f"Loading next chapter...")
    time.sleep(2)

    print("Chapter 1 completed! Saving progress...")
    save_progress(f"{next_chapter}") # Save progress before moving on

    # Load the next chapter
    return next_chapter # Return the next chapter so Game2 can load it