import json

CHOICE_FILE = "game2/choices.json"

# Ensures choices are centered dynamically
def draw_choices(screen, choices, font, screen_width, screen_height):
    max_width = max([font.size(choice)[0] for choice in choices]) + 20 # Adjust for longest text
    box_x = (screen_width - max_width) // 2 # Center the box
    box_y = screen_height * 0.75 # Place below dialogue

    for i, choice in enumerate(choices):
        text_surface = font.render(f"{i+1}. {choice}", True, (255, 255, 255))
        choice_x = box_x + (max_width - text_surface.get_width()) // 2 # Align text properly
        screen.blit(text_surface, (choice_x, box_y + i * font.get_height() * 1.5))

# Load previous choices from file or start fresh
def load_choices():
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
        return "chapter2_good.py"
    elif bad > good:
        return "chapter2_bad.py"
    else:
        return "chapter2_neutral.py" # Balanced path