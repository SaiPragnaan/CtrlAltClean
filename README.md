# 🪄 PDF Clipboard Cleaner (Linux)

A lightweight, OS-level background tool that uses local AI to instantly fix the broken formatting, arbitrary line breaks, and missing spaces you get when copying text from PDFs.

Completely local. 100% private. Zero API costs. Triggered with a single hotkey.

## 🤔 The Problem 
Copying text from a PDF is a nightmare. PDFs don't understand semantic "paragraphs"; they are just visual layouts. When you highlight and copy text, it usually pastes like this:
> This is a sentence that
> got broken in half because of
> the PDF's visual layout engine,
> and now you have to manually fix it.

## 💡 The Solution
This tool runs silently in the background on Linux. When you highlight messy text and press your custom hotkey (e.g., `Ctrl+Alt+C`), a tiny, lightning-fast local AI model (`Qwen2.5:0.5b` via Ollama) intelligently reconstructs the paragraphs and pushes the perfectly formatted text directly into your system clipboard, ready to paste.

## Features
* **Zero-Click Copy:** Reads directly from the Linux Primary Selection (just highlight text with your mouse, no need to press `Ctrl+C` first).
* **Instant Processing:** Uses an optimized, heavily quantized 0.5B parameter local LLM kept "warm" in RAM for sub-second formatting.
* **Desktop Notifications:** Native Linux `notify-send` alerts tell you when the AI starts and finishes processing.
* **Wayland & X11 Support:** Works across modern Linux desktop environments.

---

## 🛠️ Installation & Setup

### 1. Install System Dependencies
You need the native Linux clipboard managers installed. Open your terminal and run:
```bash
sudo apt-get update
sudo apt-get install xclip xsel wl-clipboard
```

### 2. Install Python Dependencies
Ensure you have Python 3 installed. Install the required Python libraries:
```bash
pip install pyperclip requests
```
### 3. Install & Setup Local AI (Ollama)
This tool uses Ollama to run the local AI model.
#### 1. Install Ollama:
```bash
curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh
```
#### Download the lightweight model (`qwen2.5:0.5b`):
```bash
ollama run qwen2.5:0.5b
```
(Once it downloads and shows a chat prompt, type `/bye` to exit. The model is now saved locally).

### 4. Clone or Save the Script
Save the Python script as `cleaner.py` anywhere on your machine (e.g., `~/Desktop/scripts/cleaner.py`).

---

## ⌨️ Configuring the OS Hotkey (Ubuntu/GNOME)
To make this work, you need to bind the script to a global system hotkey.

1. Open Settings -> Keyboard -> Keyboard Shortcuts -> View and Customize Shortcuts.

2. Scroll to the bottom and click Custom Shortcuts.

3. Click Add Shortcut (+) and fill it out:

    * Name: AI Clipboard Cleaner

    * Command: ```bash -c "/usr/bin/python3 /absolute/path/to/your/cleaner.py"```   (⚠️ Note: Replace /absolute/path/to/your/cleaner.py with the actual path to your file!)

    * Shortcut: Press Ctrl + Alt + C (or whatever you prefer).

4. Save it.

### 🛑 Troubleshooting Conda/Virtual Environments
If the hotkey doesn't work or fails silently, it is likely because your system shortcut is using the wrong Python environment.
If you use Anaconda/Miniconda, find your python path by running `which python` in your terminal. Replace `/usr/bin/python3` in the command above with that exact Conda path (e.g., `/home/username/miniconda3/bin/python`).


## 🚀 How to Use It
1. Open a PDF and highlight some messy text with your mouse.

2. Press `Ctrl + Alt + C`.

3. Wait ~2-3 seconds for the "Sanitized & Copied!" desktop notification.

4. Press Ctrl + V wherever you want to paste your beautifully formatted text.

