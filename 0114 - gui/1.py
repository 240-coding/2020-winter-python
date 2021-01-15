import tkinter

window = tkinter.Tk()

label1 = tkinter.Label(window, text = "Press any key")
label1.pack()

var = tkinter.StringVar()
var.set(' ')

label2 = tkinter.Label(window, textvariable=var)
label2.pack()

def ehandler(event) :
    var.set('key: %s' %event.char)

window.bind("<Key>", ehandler)

window.mainloop()
