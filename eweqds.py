from tkinter import *
from PIL import Image, ImageTk
import win32gui
import win32con

def setClickthrough(hwnd):
    print("setting window properties")
    try:
        styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        styles = win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
    except Exception as e:
        print(e)

# Dimensions
width = 1920 #self.winfo_screenwidth()
height = 1080 #self.winfo_screenheight()

root = Tk()
root.geometry('%dx%d' % (width, height))
root.title("Applepie")
root.attributes('-transparentcolor', 'white', '-topmost', 1)
root.config(bg='white')
root.attributes("-alpha", 0.25)
root.wm_attributes("-topmost", 1)
bg = Canvas(root, width=width, height=height, bg='white')

setClickthrough(bg.winfo_id())

frame = ImageTk.PhotoImage(file="1.png")



bg.create_image(1920/2, 1080/2, image=frame)
bg.pack()
root.mainloop()