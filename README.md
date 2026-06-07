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
2. Run:
> python main.py
3. You will get 5 seconds to open Google Docs or click any text box
4. After 5 seconds bot starts typing automatically

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

Bot randomly:
- types nearby keyboard keys
- waits shortly
- presses backspace
- types correct character

Nearby keys are stored in:

```python
KEY_NEIGHBORS = {}
```

### ESC Detection

Inside main loop:

```python
if keyboard.is_pressed("esc"):
```

This allows instant stop while typing.

### Editable Settings

Inside `main.py`:

```python
MIN_WPM, MAX_WPM = 40, 60
TYPO_CHANCE = 0.02
THINKING_PAUSE_CHANCE = 0.02
```

You can change typing speed and behaviour from here.

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

Made by Mantu Yadav

### Contact

* Discord: `your_discord_id`
* GitHub: `github.com/yourname`
* Email: `youremail@gmail.com`

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