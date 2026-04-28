from flask import Blueprint, request, render_template
from services.openai_service import generate_script
from services.voice import generate_voice
from services.thumbnail import generate_thumbnail
from models import db, Script

ai = Blueprint("ai", __name__)

@ai.route("/generate", methods=["POST"])
def generate():
    topic = request.form["topic"]

    script = generate_script(topic)
    voice = generate_voice(script)
    thumb = generate_thumbnail(topic)

    s = Script(content=script)
    db.session.add(s)
    db.session.commit()

    return render_template("dashboard.html",
                           script=script,
                           voice=voice,
                           thumb=thumb)