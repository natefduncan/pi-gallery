import os

from dotenv import load_dotenv

load_dotenv()

import glob
import random


def get_random_photo_path():
    random_file = random.choice(
        glob.glob(os.getenv("PHOTO_DIR") + "/*.jpg", recursive=True)
    )
    print(f"Selected Photo: {random_file}")
    print(os.path.join(PHOTO_DIR, random_file))
    return os.path.join(PHOTO_DIR, random_file)

def get_all_photo_paths():
    return [os.path.join(PHOTO_DIR, filepath) for filepath in glob.glob(os.getenv("PHOTO_DIR") + "/*.jpg", recursive=True)]
