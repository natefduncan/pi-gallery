from PIL import Image, ImageTk
import tkinter as tk
import requests as r
import time
from nextcloud import get_random_photo_path
import traceback
from config import SERVER_ADDRESS, SERVER_PORT
import gc


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

def PIL_to_canvas(pilImage):
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    #canvas.update()

def image_loop(delay=1):
    try:
        print("Getting image")
        img = get_image()
        img = img.rotate(270, Image.NEAREST, expand = 1)
        print("PIL to canvas")
        PIL_to_canvas(img)
        print("Canvas wait")
        canvas.after(delay*1000, image_loop)
        print("Reloop")
        #gc.collect()
        #canvas.after()
    except KeyboardInterrupt: 
        print("KEYBOARD INTERRUPT")
        quit()
    except Exception as e:
        print("ERROR")
        traceback.print_exc()
        print(e)
        quit()

if __name__=="__main__":
    root = tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()    
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))

    canvas = tk.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black', highlightthickness=0)

    image_loop()
    root.mainloop()