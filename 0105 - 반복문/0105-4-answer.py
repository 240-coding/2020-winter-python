bread = 10

while bread > 0 :
    money = int(input('현금을 입력하세요 : '))
    if money >= 500 :
        bread = bread - 1
        print('빵을 받으세요')
        if money - 500 > 0 :
            print('잔돈 : ', money - 500)
        print('남아 있는 빵의 개수 : ', bread)
    else :
        print('입력된 금액이 부족합니다.')
