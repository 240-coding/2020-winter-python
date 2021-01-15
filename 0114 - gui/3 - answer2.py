import tkinter
import math

window = tkinter.Tk()

ep = tkinter.StringVar()
entry = tkinter.Entry(window, textvariable=ep)
entry.pack(side='left')

label = tkinter.Label(window, text=' ')
label.pack(side='right')


def onClick():
    label.config(text=str(eval(ep.get())))


button = tkinter.Button(window, text='계산', command=onClick)
button.pack()

window.mainloop()
