from flask import Flask, redirect, render_template, request, flash, jsonify, send_file

from songs_model import Song

Song.load_db()

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/songs")


@app.route("/songs")
def songs():
    search = request.args.get("q")
    if search is not None:
        songs = Song.search(search)
    else:
        songs = Song.all()
    return render_template("index.html", songs=songs)
