from flask import Flask, send_file  

app = Flask(__name__)

import random

from config import SERVER_PORT
from nextcloud import get_random_photo_path


@app.route("/random-photo")
def gallery():
    image_binary = open(get_random_photo_path(),"rb")
    return send_file(
        io.BytesIO(image_binary),
        mimetype="image/jpeg",
        as_attachment=False,
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=SERVER_PORT)
