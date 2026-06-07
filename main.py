import pyautogui
import random
import string
import time

# SETTINGS

MIN_WPM,MAX_WPM= 40,60

TYPO_CHANCE = 0.02
THINKING_PAUSE_CHANCE = 0.02

open("essay.txt", "a").close()
text = open("essay.txt", "r", encoding="utf-8").read()

print("Click inside Google Docs...")
time.sleep(5)

typed_chars = 0

for ch in text:

    # Random WPM each character
    current_wpm = random.randint(MIN_WPM, MAX_WPM)

    # Convert WPM to delay
    # Average word = 5 chars
    base_delay = 60 / (current_wpm * 5)

    
    # Human typo simulation
    
    if ch.isalpha() and random.random() < TYPO_CHANCE:

        wrong = random.choice(string.ascii_lowercase)

        pyautogui.write(wrong)

        time.sleep(random.uniform(
            base_delay * 0.8,
            base_delay * 1.5
        ))

        pyautogui.press("backspace")

        time.sleep(random.uniform(
            base_delay * 0.8,
            base_delay * 1.5
        ))

    
    # Type actual character
    
    pyautogui.write(ch)

    # Base human delay
    delay = random.uniform(
        base_delay * 0.8,
        base_delay * 1.4
    )

    
    # Word pauses
    
    if ch == " ":
        delay += random.uniform(0.03, 0.12)

    # Sentence thinking pauses
    elif ch in ".!?":
        delay += random.uniform(0.4, 1.5)

    # Paragraph pause
    elif ch == "\n":
        delay += random.uniform(0.8, 2.5)

    # Random thinking pause
    if random.random() < THINKING_PAUSE_CHANCE:
        delay += random.uniform(0.5, 2)

    # Slight fatigue slowdown
    typed_chars += 1
    delay += typed_chars * 0.000002

    time.sleep(delay)

print("Finished typing.")