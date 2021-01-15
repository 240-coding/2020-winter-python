import tkinter
window = tkinter.Tk()

label1 = tkinter.Label(window, text='Press any key')
label1.pack()

data = tkinter.StringVar()
data.set(' ')

label2 = tkinter.Label(window, textvariable=data)
label2.pack()


def pressKey(event):
    data.set(event.char)


window.bind("<Key>", pressKey)

window.mainloop()
