import glob
import os
import random

from config import PHOTO_DIR


def get_random_photo_path():
    random_file = random.choice(glob.glob(PHOTO_DIR + "/*.jpg", recursive=True))
    print(f"Selected Photo: {random_file}")
    print(os.path.join(PHOTO_DIR, random_file))
    return os.path.join(PHOTO_DIR, random_file)
