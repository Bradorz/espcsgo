import time
import tkinter as tk

Width = 1920
Height = 1080

root = tk.Tk()
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.wm_attributes("-toolwindow", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")
root.update()

canvas = tk.Canvas(root, width=Width, height=Height, bg='white')
canvas.pack()

while 1:
    root.update()
    canvas.create_rectangle(0, 0, 555, 511, fill='white')