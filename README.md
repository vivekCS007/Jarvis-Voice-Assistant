# Jarvis Voice Assistant 🧠🎤

A Python-based voice assistant with automation capabilities that:
- Activates with "Jarvis" voice command
- Supports voice recognition and response
- Uses gTTS + pygame for speech output
- Can open popular websites
- Fetches headlines using NewsAPI
- Generates responses using Gemini AI
- **NEW:** Automated chat reply system with cursor position tracking
- **NEW:** Browser automation for drag, copy, and paste operations

## Features

### Voice Assistant
- Wake word detection ("Jarvis")
- Voice-to-text conversion
- Text-to-speech responses
- Website navigation commands
- News headline fetching

### Chat Automation (New)
- **Automated Reply Generation**: Intelligently generates responses as "Vivek" persona
- **Cursor Position Tracking**: Real-time mouse coordinate detection for precise automation
- **Smart Chat Detection**: Analyzes chat history to avoid duplicate replies
- **Drag & Drop Automation**: Automatically selects, copies, and replies to messages

## Setup

### Prerequisites
- Python 3.7+
- Active internet connection
- Microphone access
- Screen access permissions (for automation features)

### Installation
1. Clone the repository
2. Make an virtual environment(optional but recommended)
   ```bash
   python3 -m venv venv
    ```
   To activate it:
   1. In Linux/Macos
      ```bash
       source venv/bin/activate
      ```
   2. In Windows
      ```bash
      venv\Scripts\Activate.ps1
      ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a .env file:
   ```bash
   NEWS_API=your_newsapi_key
   GEMINI_API=your_gemini_key
   ```

5. Run the assistant:
   ```bash
   python main.py
   ```
   in windows.
   ```bash
   python main.py 2> /dev/null
   ```
   in linux to avoid asla warnings.

    

### Chat Automation

#### 1. Get Cursor Positions
Use `get_cursor_position.py` to find exact coordinates for your chat application:

```bash
python get_cursor_position.py
```

- Move your mouse to different positions in your chat window
- Note the coordinates printed in the terminal
- Update the coordinates in `bot.py` if needed:
  - Start position: `(727, 204)`
  - End selection: `(1883, 994)`
  - Text input field: `(843, 1039)`
  - Click area: `(33, 390)`

#### 2. Automated Reply System
Run the only automated chat reply system:

```bash
python bot.py 
```

**How it works:**
1. **Preparation**: You have 5 seconds to switch to your chat application window
2. **Message Detection**: Automatically drags to select the latest messages
3. **Content Analysis**: Copies and analyzes the chat history
4. **Smart Reply**: Generates contextual responses as "Vivek" persona
5. **Auto-Send**: Pastes and sends the AI-generated reply
6.  This will run once 