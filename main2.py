from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.title('Tkinter - GUI framework')
window.resizable(height=True, width=True)
window.minsize(450, 300)

Label(window, text='Hello, Tkinter.....', justify=CENTER,
      relief=SUNKEN).pack(pady=10)

image = Image.open('Python_Logo.png')
image = image.resize((200, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
frame = Frame(window, width=250, height=200, background='black')
frame.pack_propagate(0)
frame.pack()
Label(frame, image=photo).pack()

window.mainloop()
