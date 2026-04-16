import pyperclip
import os
import subprocess
import requests

def get_highlighted_text():
    try:
        return subprocess.check_output(['wl-paste', '-p'], text=True)
    except Exception:
        pass
    
    try:
        return subprocess.check_output(['xclip', '-o', '-selection', 'primary'], text=True)
    except Exception:
        return ""

def clean_and_process_text(text):
    url="http://localhost:11434/api/generate"
    prompt = f"Fix the formatting, accidental line breaks, and spacing of this extracted PDF text. Do not add any conversational filler. Output ONLY the perfectly formatted text(DO NOT add any new text):\n##TEXT:\n\n{text}"
    payload={
            "model":"qwen2.5:0.5b",
            "prompt":prompt,
            "stream":False,
            "keep_alive": -1,
            "options": {
            "temperature": 0.0, 
            "num_predict": 2048,
            "num_thread": 4
        }
        }
    try:
        response=requests.post(url, json=payload)
        return response.json().get("response","").replace("### TEXT:","").strip()
    except Exception as e:
        return f"AI Error: Make sure Ollama is running! ({e})"
    

def clean_pdf_text():
    raw_text = get_highlighted_text()
    
    if not raw_text or len(raw_text.strip()) == 0:
            os.system('notify-send "AI Cleaner" "No text highlighted."')
            return

    os.system('notify-send "AI Cleaner" "Processing text..."')
    
    cleaned_text = clean_and_process_text(raw_text)

    pyperclip.copy(cleaned_text)
    
    os.system('notify-send "AI Cleaner" "Sanitized & Copied! Ready to paste."')

clean_pdf_text()