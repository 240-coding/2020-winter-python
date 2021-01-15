import tkinter
window = tkinter.Tk()

label = tkinter.Label(window, text="Hello, Python",
                      bg="Black", fg="Yellow", font=("Times", 48, "bold"))
label.pack()

window.mainloop()
