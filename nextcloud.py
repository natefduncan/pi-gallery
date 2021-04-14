import glob
import os
import random

from dotenv import load_dotenv
from PIL import Image

from rotate import autorotate

load_dotenv()
PHOTO_DIR = os.getenv("PHOTO_DIR")


def get_random_photo_path():
    random_file = random.choice(
        glob.glob(PHOTO_DIR + "/*.jpg", recursive=True)
    )
    print(f"Selected Photo: {random_file}")
    print(os.path.join(PHOTO_DIR, random_file))
    return os.path.join(PHOTO_DIR, random_file)


def get_random_PIL():
    path = get_random_photo_path()
    img = Image.open(path)
    return autorotate(img)
