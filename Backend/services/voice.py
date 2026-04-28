from gtts import gTTS
import os

def generate_voice(text):
    os.makedirs("frontend/static", exist_ok=True)
    
    # Text-to-Speech ko save karna
    path = "frontend/static/voice.mp3"
    gTTS(text).save(path)
    
    return "/static/voice.mp3"