from PIL import Image, ImageDraw
import os

def generate_thumbnail(text):
    # Ye line automatically 'static' folder bana degi agar nahi hoga toh
    os.makedirs("frontend/static", exist_ok=True)
    
    img = Image.new("RGB", (1280, 720), color="black")
    draw = ImageDraw.Draw(img)
    
    # Image par text likhna
    draw.text((100, 300), text[:30], fill="white")

    # File ko system me save karna
    img.save("frontend/static/thumb.png")
    
    # Browser ko display karne ke liye sahi link dena
    return "/static/thumb.png"