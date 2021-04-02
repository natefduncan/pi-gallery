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
        self.wm_geometry("0x0+0+0")

        self.window = MySlideShow(self)
        self.window.startSlideShow()


class MySlideShow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        #remove window decorations 
        self.overrideredirect(True)

        #save reference to photo so that garbage collection
        #does not clear image variable in show_image()
        self.persistent_image = None
        self.imageList = []
        self.pixNum = 0

        #used to display as background image
        self.label = tk.Label(self)
        self.label.pack(side="top", fill="both", expand=True)

    def getImages(self):
        '''
        Get image directory from command line or use current directory
        '''
        if len(sys.argv) == 2:
            curr_dir = sys.argv[1]
        else:
            curr_dir = '.'

        for root, dirs, files in os.walk(curr_dir):
            for f in files:
                if f.endswith(".png") or f.endswith(".jpg"):
                    img_path = os.path.join(root, f)
                    print(img_path)
                    self.imageList.append(img_path)

    def startSlideShow(self, delay=10): #delay in seconds
        get_image()
        self.showImage("temp.jpg")
        #its like a callback function after n seconds (cycle through pics)
        self.after(delay*1000, self.startSlideShow)

    def showImage(self, filename):
        image = Image.open(filename)  

        img_w, img_h = image.size
        scr_w, scr_h = self.winfo_screenwidth(), self.winfo_screenheight()
        width, height = min(scr_w, img_w), min(scr_h, img_h)
        image.thumbnail((width, height), Image.ANTIALIAS)

        #set window size after scaling the original image up/down to fit screen
        #removes the border on the image
        scaled_w, scaled_h = image.size
        self.wm_geometry("{}x{}+{}+{}".format(scaled_w,scaled_h,0,0))
        
        # create new image 
        self.persistent_image = ImageTk.PhotoImage(image)
        self.label.configure(image=self.persistent_image)

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
    slideShow = HiddenRoot()
    slideShow.bind("<Escape>", lambda e: slideShow.destroy())  # exit on esc
    slideShow.mainloop()