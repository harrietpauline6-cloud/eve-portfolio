"""Small Flask app for Eve's personal portfolio."""

from pathlib import Path

from flask import Flask, render_template, send_file


ROOT = Path(__file__).resolve().parent
app = Flask(__name__, static_folder="static", template_folder="templates")


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/profile-picture")
def profile_picture():
    """Serve the supplied Evee.png image without exposing the project directory."""
    image_path = ROOT / "Evee.png"
    if not image_path.is_file():
        return "Profile photo not found. Add Evee.png to the project folder.", 404
    return send_file(image_path, conditional=True, max_age=3600)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
