from flask import Flask, render_template
import io
import requests as r
from config import SERVER_ADDRESS, SERVER_PORT, DELAY
from nextcloud import get_random_photo_path
from config import GALLERY_PORT
from PIL import Image
import webbrowser
from threading import Timer

app = Flask(__name__)

def get_image():
    url = f"http://{SERVER_ADDRESS}:{SERVER_PORT}/random-photo"
    response = r.get(url, stream=True)
    if response.status_code == 200:
        with open(r"static/temp.jpg", 'wb') as f:
            f.write(response.content)
        img = Image.open("static/temp.jpg")
        return img
    else:
        return None

@app.route("/")
def gallery():
    img = get_image()
    img = img.rotate(270, Image.NEAREST, expand = 1)
    width, height = img.size
    img.save("static/temp.jpg")
    return render_template("gallery.html", delay=DELAY, width=width, height=height)

def open_browser():
      webbrowser.open_new('http://127.0.0.1:8080/')    

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(port=GALLERY_PORT)
