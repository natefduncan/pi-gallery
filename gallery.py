from PIL import Image, ImageTk
import tkinter
import requests as r
import time
from config import SERVER_ADDRESS, SERVER_PORT

def create_canvas():
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()    
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    return [canvas, w, h]

def PIL_to_canvas(pilImage, canvas, w, h):
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)

def get_image():
    url = f"http://{SERVER_ADDRESS}:{SERVER_PORT}/random-photo"
    response = r.get(url, stream=True)
    if response.status_code == 200:
        with open(r"temp.jpg", 'wb') as f:
            f.write(response.content)
        img = Image.open("temp.jpg")
        return img
    else:
        return None

def image_loop():
    canvas, w, h = create_canvas()
    while True:
        try:
            img = get_image()
            img = img.rotate(270, Image.NEAREST, expand = 1)
            PIL_to_canvas(img, canvas, w, h)
            time.sleep(5)
        except KeyboardInterrupt:
            break

if __name__=="__main__":
    image_loop()