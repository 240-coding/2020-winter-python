import tkinter
import math  # math 모듈 임포트

window = tkinter.Tk()
cal = tkinter.StringVar()
cal.set(' ')

result = tkinter.StringVar()
result.set(' ')


def printResult():
    result.set(str(eval(cal.get())))  # get() 함수를 이용해서 변수의 값을 불러와야 함


label1 = tkinter.Label(window, text="계산할 수식을 입력하세요")
label1.pack()
entry = tkinter.Entry(window, textvariable=cal)
entry.pack()
button = tkinter.Button(window, text="계산", command=printResult)
button.pack()
label2 = tkinter.Label(window, textvariable=result)
label2.pack()

window.mainloop()
