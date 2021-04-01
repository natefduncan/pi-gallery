from flask import Flask, send_file  
import io

app = Flask(__name__)

import random

from config import SERVER_PORT
from nextcloud import get_random_photo_path


@app.route("/random-photo")
def gallery():
    return send_file(
        get_random_photo_path(),
        mimetype="image/jpeg",
        as_attachment=True,
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=SERVER_PORT)
