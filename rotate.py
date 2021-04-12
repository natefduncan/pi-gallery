import sys
from PIL import Image

def rotate_and_save(file_path):
    og_image = Image.open(file_path)
    rot_image = Image.rotate(270)
    rot_image.save(file_path)

def autorotate(path):
    """ This function autorotates a picture """
    image = Image.open(path)
    try:
        exif = image._getexif()
    except AttributeError as e:
        print("Could not get exif - Bad image!")
        return False

    (width, height) = image.size
    # print "\n===Width x Heigh: %s x %s" % (width, height)
    if not exif:
        if width > height:
            image = image.rotate(90)
            image.save(path, quality=100)
            return True
    else:
        orientation_key = 274 # cf ExifTags
        if orientation_key in exif:
            orientation = exif[orientation_key]
            rotate_values = {
                3: 180,
                6: 270,
                8: 90
            }
            if orientation in rotate_values:
                # Rotate and save the picture
                image = image.rotate(rotate_values[orientation])
                image.save(path, quality=100, exif=exif)
                return True
        else:
            if width > height:
                image = image.rotate(90)
                image.save(path, quality=100, exif=exif)
                return True

    return False

if __name__=="__main__":
    rotate_and_save(sys.argv[1])
