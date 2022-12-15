from tkinter import *

window = Tk()
window.title('Confirm Dialog')

label = Label(window, text='Are you sure you want to exit?')
label.pack(pady=10)
Button(window, text='No').pack(side=RIGHT)
Button(window, tet='Yes', command=window.quit).pack(side=RIGHT)

window.mainloop()
