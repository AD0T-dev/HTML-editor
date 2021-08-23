from tkinter import *
from tkinter.filedialog import *

win = Tk()

win.title("HTML EDITOR")

win.minsize(500,500)

win.maxsize(800,500)

entr = Text(win,width=100,height=30)
entr.grid(columnspan=10,row=2,column=1)


def open_file():

    file = askopenfile(title="open_file")

    if file is not None:
        entr.delete('1.0',END)

        items = file.readlines()

        for item in items:
            entr.insert(END, item.strip())

def save_file():

    file2 = asksaveasfile(defaultextension=".html")

    if file2 is not None:
        entr.delete('1.0',END)

open_btn = Button(win,text="OPEN", command=open_file,width=20)
save_btn = Button(win,text="SAVE", command=save_file,width=20)

open_btn.grid(column=0,row=1,columnspan=4)
save_btn.grid(column = 3,row=1,columnspan=4)

win.mainloop()
