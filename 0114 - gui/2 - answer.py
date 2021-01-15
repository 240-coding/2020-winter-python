import tkinter

window = tkinter.Tk()

label = tkinter.Label(window, text = "Hello, Python",
                      bg = "black", fg = "yellow",
                      font = ("times", 48, "bold"))
label.pack()

window.mainloop()
