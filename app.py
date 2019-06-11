import os
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    images = os.listdir('./images')
    return render_template("gallery.html", image_names=images)

@app.route("/list")
def gallery_index():
    images = os.listdir('./images')
    return render_template("gallery_index.html", image_names=images)

@app.route('/images/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run()