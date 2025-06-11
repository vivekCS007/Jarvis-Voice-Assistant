# Jarvis Voice Assistant 🧠🎤

A Python-based voice assistant that:
- Activates with "Jarvis"
- Supports voice recognition and response
- Uses gTTS + pygame for speech output
- Can open popular websites
- Fetches headlines using NewsAPI
- Generates responses using Gemini AI

## Setup

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

    
