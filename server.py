import io
import os
import random

from dotenv import load_dotenv
from flask import Flask, send_file

from nextcloud import get_random_photo_path

load_dotenv()
app = Flask(__name__)


@app.route("/random-photo")
def gallery():
    return send_file(
        get_random_photo_path()
        mimetype="image/jpeg",
        as_attachment=True,
    )

@app.route("/urls")
def urls():
    

@app.route("/photo")
def photo():
    filepath = request.args.get("filepath")
    return send_file(
        filepath, 
        mimetype="image/jpeg",
        as_attachment=True,
    )



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("SERVER_PORT"))
