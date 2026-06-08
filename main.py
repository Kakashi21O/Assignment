import subprocess
import sys
import importlib

# Auto install modules
modules = [
    "pyautogui",
    "keyboard"
]

for module in modules:

    try:
        importlib.import_module(module)

    except ImportError:

        print(f"Installing {module}...")

        try:
            subprocess.check_call([
                sys.executable,
                "-m",
                "ensurepip",
                "--upgrade"
            ])

            subprocess.check_call([
                sys.executable,
                "-m",
                "pip",
                "install",
                module
            ])

        except Exception as e:
            print(f"Failed installing {module}")
            print(e)
            sys.exit()


import pyautogui
import keyboard
import random
import string
import time

pyautogui.FAILSAFE = True

# ESC stop system
stop_typing = False

def stop():
    global stop_typing
    stop_typing = True
    print("Stopped by user.")

keyboard.add_hotkey("esc", stop)

# SETTINGS

MIN_WPM,MAX_WPM= 40,60

TYPO_CHANCE = 0.02
THINKING_PAUSE_CHANCE = 0.02

open("essay.txt", "a").close()
text = open("essay.txt", "r", encoding="utf-8").read()

print("Click inside Google Docs...")
time.sleep(5)

typed_chars = 0

#delay in words helping variable
current_word = ""

# Nearby keyboard keys
KEY_NEIGHBORS = {
    "a": "sqwz",
    "b": "vghn",
    "c": "xdfv",
    "d": "serfcx",
    "e": "wsdr",
    "f": "drtgcv",
    "g": "ftyhbv",
    "h": "gyujnb",
    "i": "ujko",
    "j": "huikmn",
    "k": "jiolm",
    "l": "kop",
    "m": "njk",
    "n": "bhjm",
    "o": "iklp",
    "p": "ol",
    "q": "wa",
    "r": "edft",
    "s": "awedxz",
    "t": "rfgy",
    "u": "yhji",
    "v": "cfgb",
    "w": "qase",
    "x": "zsdc",
    "y": "tghu",
    "z": "asx"
}

for ch in text:
    
    # Press ESC to stop
    if stop_typing:
        break

    # Random WPM each character
    current_wpm = random.randint(MIN_WPM, MAX_WPM)

    # Convert WPM to delay
    # Average word = 5 chars
    base_delay = 60 / (current_wpm * 5)

    
    # Human typo simulation
    
    if ch.isalpha() and random.random() < TYPO_CHANCE:

        #            wrong funtioning logic start
        lower_ch = ch.lower()

        if lower_ch in KEY_NEIGHBORS:
            wrong = random.choice(KEY_NEIGHBORS[lower_ch])

            # preserve uppercase
            if ch.isupper():
                wrong = wrong.upper()
        else:
            wrong = random.choice(string.ascii_lowercase)
       
        pyautogui.write(wrong)
        #           end
        
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

    # Track current word
    if ch not in " \n\t":
        current_word += ch
    else:

        # Pause after completing a word
        if current_word:

            word_length = len(current_word)

            # Longer words = slightly longer pause
            word_pause = random.uniform(
                0.04,
                0.12 + (word_length * 0.01)
            )

            delay += word_pause

        current_word = ""
    time.sleep(delay)

print("Finished typing.")