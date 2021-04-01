from PIL import Image
import requests as r
from config import SERVER_ADDRESS, SERVER_PORT

def get_image():
    url = f"http://{SERVER_ADDRESS}:{SERVER_PORT}/random-photo"
    response = r.get(url, stream=True)
    if response.status_code == 200:
        with open(r"temp.jpg", 'wb') as f:
            f.write(response.content)
        img = Image("temp.jpg")
        img.show()


if __name__=="__main__":
    get_image()