from flask import Flask, render_template
from models import db
from routes.auth import auth
from routes.ai import ai

app = Flask(__name__, 
            template_folder="../frontend", 
            static_folder="../frontend/static")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(ai)

@app.route("/")
def home():
    return render_template("index.html")
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
app.run(debug=True)