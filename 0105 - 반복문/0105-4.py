bread = 10
while bread > 0 :
    money = int(input('현금을 입력하세요 : '))
    if money >= 500 :
        bread -= 1
        print('잔돈 : %d원\n남은 빵 : %d개' %(money - 500, bread))
    else :
        print('금액이 부족합니다.')
