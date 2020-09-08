#CMD LIST
#env\Scripts\activate.bat
#set FLASK_RUN=app.py
#set FLASK_ENV=development
#flask run
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run()