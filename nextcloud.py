import glob
import os
import random

from dotenv import load_dotenv
from PIL import Image

from rotate import autorotate

load_dotenv()



def get_random_photo_path():
    random_file = random.choice(
        glob.glob(os.getenv("PHOTO_DIR") + "/*.jpg", recursive=True)
    )
    print(f"Selected Photo: {random_file}")
    print(os.path.join(PHOTO_DIR, random_file))
    return os.path.join(PHOTO_DIR, random_file)


def get_random_PIL():
    path = get_random_photo_path()
    return autorotate(Image(path))
