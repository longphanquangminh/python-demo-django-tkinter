from tkinter import *

window = Tk()
window.title('Tkinter')

Label(window, text="Enter your email:").pack(side=LEFT, pady=10, padx=5)
email = StringVar()
email.set('iloveuel@uel.edu.vn')
Entry(window, textvariable=email, width=20).pack(side=LEFT)
Button(window, text="OK", highlightbackground='cyan').pack(side=RIGHT, pady=10)

window.mainloop()
