import tkinter
import math
window = tkinter.Tk()

frame = tkinter.Frame(window, borderwidth = 2, relief = tkinter.GROOVE)
frame.pack()

ep = tkinter.StringVar()
entry = tkinter.Entry(frame, textvariable = ep)
entry.pack(side = 'left')

label = tkinter.Label(frame, text=' ')
label.pack(side = 'right')

def onClick() :
    label.config(text = str(eval(ep.get())))

button = tkinter.Button(window, text = '계산', command = onClick)
button.pack()

window.mainloop()
