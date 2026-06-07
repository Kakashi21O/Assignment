import pyautogui
import random
import string
import time

text = "Hello every one nice to meet you"

print("Click in Google Docs...")
time.sleep(5)

for ch in text:

    # 2% chance of typo
    if ch.isalpha() and random.random() < 0.02:
        wrong = random.choice(string.ascii_lowercase)

        pyautogui.write(wrong)
        time.sleep(random.uniform(0.05, 0.15))

        pyautogui.press("backspace")
        time.sleep(random.uniform(0.05, 0.20))

    pyautogui.write(ch)

    delay = random.uniform(0.04, 0.14)

    if ch in ".!?":
        delay += random.uniform(0.3, 1.2)

    elif ch == " ":
        delay += random.uniform(0.01, 0.08)

    time.sleep(delay)