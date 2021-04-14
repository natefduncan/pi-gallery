import io
import os
import random
from io import BytesIO

from dotenv import load_dotenv
from flask import Flask, send_file

from nextcloud import get_random_PIL
from rotate import autorotate

load_dotenv()
app = Flask(__name__)


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, "JPEG", quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype="image/jpeg")


@app.route("/random-photo")
def gallery():
    pil = get_random_PIL()
    return serve_pil_image(pil)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("SERVER_PORT"))
