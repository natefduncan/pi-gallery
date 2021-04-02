from PIL import Image, ImageTk
import tkinter as tk
import requests as r
import time
from nextcloud import get_random_photo_path
from config import SERVER_ADDRESS, SERVER_PORT

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

class HiddenRoot(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #hackish way, essentially makes root window
        #as small as possible but still "focused"
        #enabling us to use the binding on <esc>
        self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (self.w, self.h))

        self.window = MySlideShow(self)
        self.window.startSlideShow()


class MySlideShow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        #remove window decorations 
        self.overrideredirect(True)
        self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()

        #save reference to photo so that garbage collection
        #does not clear image variable in show_image()
        self.persistent_image = None
        self.imageList = []
        self.pixNum = 0

        #used to display as background image
        self.label = tk.Label(self)
        self.label.pack(side="top", fill="both", expand=True)

    def startSlideShow(self, delay=10): #delay in seconds
        img = get_image()
        img = img.rotate(270, Image.NEAREST, expand = 1)
        self.showImage(img)
        #its like a callback function after n seconds (cycle through pics)
        self.after(delay*1000, self.startSlideShow)

    def showImage(self, image):
        #Canvas
        self.focus_set()
        canvas = tk.Canvas(self, width=self.w, height=self.h)
        canvas.pack()
        canvas.configure(background='black')
        
        # create new image 
        imgWidth, imgHeight = image.size
        if imgWidth > self.w or imgHeight > self.h:
            ratio = min(self.w/imgWidth, self.h/imgHeight)
            imgWidth = int(imgWidth*ratio)
            imgHeight = int(imgHeight*ratio)
            pilImage = image.resize((imgWidth,imgHeight), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        imagesprite = canvas.create_image(self.w/2,self.h/2,image=image)

def PIL_to_canvas(pilImage):
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    canvas.update()

def image_loop(delay=1):
    try:
        print("Getting image")
        img = get_image()
        img = img.rotate(270, Image.NEAREST, expand = 1)
        print("PIL to canvas")
        PIL_to_canvas(img)
        time.sleep(5)
        print("After")
        canvas.after(0, image_loop)
    except KeyboardInterrupt: 
        quit()

if __name__=="__main__":
    root = tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w-200, h-200))
    root.focus_set()    
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))

    canvas = tk.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black', highlightthickness=0)

    image_loop()
    root.mainloop()

    '''
    slideShow = HiddenRoot()
    slideShow.bind("<Escape>", lambda e: slideShow.destroy())  # exit on esc
    slideShow.mainloop()
    '''