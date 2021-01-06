light = float(input('밝기를 입력하세요 : '))
temp = float(input('온도를 입력하세요 : '))

if light < 0.01 or temp >= 0 :
    print('스위치 : ON')
else :
    print('스위치 : OFF')
