import tkinter
window = tkinter.Tk()

label1 = tkinter.Label(window, text='Press any key')
label1.pack()


def pressKey(event):
    data = tkinter.StringVar()
    data.set(event.char)
    label2 = tkinter.Label(window, textvariable=data)
    label2.pack()


frame = tkinter.Frame(window, width=300, height=300)
frame.bind("<Key>", pressKey)
frame.pack()

window.mainloop()
