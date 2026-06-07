# Human Typing Bot

Simple Python bot that types text like a human in Google Docs or any text field.

<br>
<br>

---

<br>
<br>
<br>
<br>
<br>
<br>

## ✦ User Manual

### Setup

1. Put your text inside `essay.txt`
2. Run: `python main.py`
1. You will get 5 seconds to open Google Docs or click any text box
2. After 5 seconds bot starts typing automatically

### ESC Shortcut

- Press `ESC` anytime to stop the bot instantly

### Files

- `essay.txt` → text that will be typed
- `requirements.txt` → libraries auto installed on start
- `main.py` → main typing bot code

### Features

- Human typing speed
- Random typing mistakes
- Backspace correction
- Small thinking pauses
- Sentence and paragraph delay
- Auto install requirements

<br>
<br>

---

<br>
<br>
<br>
<br>
<br>
<br>

## ✦ Developer Notes

### Workflow

1. Check if `requirements.txt` exists
2. Auto install missing libraries using pip
3. Read text from `essay.txt`
4. Wait 5 seconds for user setup
5. Start character-by-character typing
6. Detect `ESC` key every loop
7. Add human behaviour delays and typo logic
8. Stop after text ends or ESC pressed

### Main Libraries

- `pyautogui` → keyboard typing
- `keyboard` → ESC detection
- `random` → random delays and mistakes
- `time` → sleep and pause handling
- `subprocess` → pip install command

### Typing Logic

- WPM changes randomly between min and max values
- Delay is calculated from WPM
- Longer pauses after:
  - spaces
  - sentences
  - paragraphs

### Typo System

- Bot randomly types nearby keyboard keys
- It randomly waits shortly
- It randomly presses backspace

### Nearby Key Detection

* Nearby keyboard keys are stored inside:
  `KEY_NEIGHBORS = {}`

* This is used for realistic typing mistakes by checking nearby keys on the keyboard.

### ESC Detection

* Inside the main loop:
  `if keyboard.is_pressed("esc"):`

* This allows the program to stop instantly when the `ESC` key is pressed.

### Editable Settings

* Inside `main.py` :&emsp;
  `MIN_WPM, MAX_WPM = 40, 60`
  `TYPO_CHANCE = 0.02`
  `THINKING_PAUSE_CHANCE = 0.02`

* You can edit these values to change typing speed, typo frequency, and thinking pauses.

<br>
<br>

---

<br>
<br>
<br>
<br>
<br>
<br>

## ✦ My Details

### Developer

Made by Nova

### Contact

* Discord: [`electro_blaz`](https://discord.com/users/342966677022965762)
* GitHub: [`Kakashi21O`](https://github.com/Kakashi21O)
* Email: [`kakashi7gamer@gmail.com`](mailto:kakashi7gamer@gmail.com)

### Other Projects

If you liked this project, please check out my other projects on GitHub.

#### Feel free to use or modify any project.

<br>
<br>

---

<br>
<br>
<br>
<br>
<br>
<br>