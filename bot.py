import pyautogui
import time
import pyperclip
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gemini API setup
GEMINI_API = os.getenv("GEMINI_API")
if GEMINI_API:
    genai.configure(api_key=GEMINI_API)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    print("Gemini API key is missing.")
    model = None

# Check if Vivek replied last
def should_reply(chat_history):
    lines = chat_history.strip().split("] ")
    for line in reversed(lines):
        line = line.strip()
        if line:
            return "2024CA115_Vivek Sharma:" not in line
    return False

# AI reply generation
def aiprocess(command):
    if not model:
        print("AI is not available because the API key is missing.")
        return ""

    try:
        prompt = f"""
You are Vivek — a coder from India who speaks Hindi and English, and you tend to respond with confidence, clarity, and a touch of friendliness. Your tone is direct yet approachable.

Below is a piece of copied text from a chat or article:
\"\"\"{command}\"\"\"

Analyze the above text and respond naturally like Vivek would. If it's a conversation, reply with what Vivek would say next. If it's information, summarize or react informally like you're explaining it to a friend.

Prefer using English, but mix Hindi for expressions if it feels natural. Keep it short and engaging — ideally 2 sentences.
"""
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("Error with Gemini API:", e)
        return ""

# ✅ Unified one-time task: drag, copy, reply
def reply():
    print("🤖 Executing drag + AI reply")

    # Drag and select message
    pyautogui.moveTo(727, 204, duration=0.5)
    pyautogui.mouseDown()
    pyautogui.moveTo(1883, 994, duration=1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    # Copy selected message
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    # Click elsewhere to unselect
    pyautogui.moveTo(1833, 700, duration=0.5)
    pyautogui.click()

    # Read clipboard
    chat_history = pyperclip.paste()
    print("📋 Copied text:\n", chat_history)

    # Process if Vivek hasn't replied last
    if should_reply(chat_history):
        ai_response = aiprocess(chat_history)
        if ai_response:
            pyperclip.copy(ai_response)
            time.sleep(0.3)

            # Paste and send
            pyautogui.moveTo(843, 1039, duration=0.5)
            pyautogui.click()
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.2)
            pyautogui.press('enter')
            print("✅ AI reply sent.")
        else:
            print("⚠️ No response generated.")
    else:
        print("✅ Vivek already replied — skipping.")

# 🔁 Full loop if run directly
def start_auto_reply_loop():
    print("Starting automation in 5 seconds... Switch to the correct window.")
    time.sleep(5)

    pyautogui.moveTo(33, 390, duration=0.5)
    pyautogui.click()
    time.sleep(1)

    try:
        while True:
            print("\n🔁 Checking for new message...")
            reply()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n🛑 Automation stopped manually.")

# 🎯 Entry point
if __name__ == "__main__":
    start_auto_reply_loop()
