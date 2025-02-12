import json
import os

CHOICE_FILE = "game2/choices.json"

# Ensures choices are centered dynamically
def draw_choices(screen, choices, font, screen_width, dialogue_box_bottom):
    # Dynamically determine the max width for the longest choice
    max_width = max([font.size(choice)[0] for choice in choices]) + 20 # Adjust for longest text
    box_x = (screen_width - max_width) // 2  # Center the box horizontally

    # Start placing choices below the dialogue box, adjusting for dialogue length
    y_offset = dialogue_box_bottom + 20  # Add some padding to separate dialogue from choices

    for i, choice in enumerate(choices):
        text_surface = font.render(f"{i+1}. {choice}", True, (255, 255, 255))
        choice_x = box_x + (max_width - text_surface.get_width()) // 2  # Center the text
        screen.blit(text_surface, (choice_x, y_offset + i * font.get_height() * 1.5))  # Spacing between choices

# Load previous choices from file or start fresh
def load_choices():
    if not os.path.exists(CHOICE_FILE):
        return {"good": 0, "bad": 0} # Default values if file is missing

    try:
        with open(CHOICE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"good": 0, "bad": 0} # Default: No choices made

# Save the player's choices (good/bad)
def save_choice(choice_type):
    choices = load_choices()

    if choice_type == "good":
        choices["good"] += 1
    elif choice_type == "bad":
        choices["bad"] += 1

    with open(CHOICE_FILE, "w") as file:
        json.dump(choices, file)

# Determine the next chapter based on choice balance
def determine_next_chapter():
    choices = load_choices()
    good = choices["good"]
    bad = choices["bad"]

    if good > bad:
        return "chapter2_good"
    elif bad > good:
        return "chapter2_bad"
    else:
        return "chapter2_neutral" # Balanced path