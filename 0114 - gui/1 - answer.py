import tkinter

window = tkinter.Tk()

label1 = tkinter.Label(window, text="Press any key")
label1.pack()

label2 = tkinter.Label(window, text=' ')
label2.pack()


def ehandler(event):  # 이벤트가 발생하면 label2 내용 수정
    label2.config(text='key: %s' % event.char)


window.bind("<Key>", ehandler)  # window에 이벤트 바인딩

window.mainloop()
