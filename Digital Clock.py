from tkinter import *
from tkinter.ttk import *
from time import strftime

main = Tk()
main.title('Digital Clock by Josh')

image_icon=PhotoImage(file="Sand-Timer-128.png")
main.iconphoto(False,image_icon)

main.resizable(False,False)


def none():
    text=strftime(' %a %H:%M:%S %p %z')
    lbl.config(text=text)
    lbl.after(1000, none)
lbl=Label(main, font=('OCR A Extended', 50, 'bold'), background= 'white', foreground='#154c79')
lbl.pack(anchor='center')

none()


mainloop()
