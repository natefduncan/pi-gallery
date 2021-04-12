import sys
from PIL import Image

def rotate_and_save(file_path):
    og_image = Image.open(file_path)
    rot_image = Image.rotate(270)
    rot_image.save(file_path)

if __name__=="__main__":
    rotate_and_save(file_path(sys.argv[0]))
