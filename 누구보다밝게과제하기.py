import tkinter
window = tkinter.Tk()

radioValue = tkinter.IntVar()

button1 = tkinter.Radiobutton(window, text="누구보다 밝게 과제하기♥", variable = radioValue, value=1)
button1.pack()
button2 = tkinter.Radiobutton(window, text="뭐든 잘 하려고 노력하기♥", variable = radioValue, value=2)
button2.pack()
button3 = tkinter.Radiobutton(window, text="지랄하네씨발럼들살인살인", variable = radioValue, value=3)
button3.pack()

window.mainloop()
