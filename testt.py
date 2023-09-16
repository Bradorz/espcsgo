from tkinter import *


# Create object
root = Tk()


Label(root, text="This window will always stay on Top", font=('Aerial 14')).pack(pady=30, anchor =CENTER)
# Adjust size
root.geometry("800x600")
root.lift()
root.attributes('-alpha',0.5)
root.attributes('-topmost',True)
#oot.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")
root.overrideredirect(True)
# Execute tkinter
root.mainloop()