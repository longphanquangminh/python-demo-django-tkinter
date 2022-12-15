from tkinter import *
window = Tk()
window.title('Tkinter - GUI framework')
window.resizable(height=True, width=True)
window.minsize(500, 350)
# Center Screen
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth()//2) - (width//2)
y = (window.winfo_screenheight()//2) - (height//2)
window.geometry(f'{width}x{height}+{x}+{y}')
# Draw UI
window.mainloop()
