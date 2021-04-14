import sys

from PIL import ExifTags, Image


def rotate_and_save(file_path):
    og_image = Image.open(file_path)
    rot_image = og_image.rotate(270)
    rot_image.save(file_path)

def autorotate(image)
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        
        exif = image._getexif()

        if exif[orientation] == 3:
            image=image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image=image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image=image.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        # cases: image don't have getexif
        pass
    return image

if __name__=="__main__":
    rotate_and_save(sys.argv[1])
