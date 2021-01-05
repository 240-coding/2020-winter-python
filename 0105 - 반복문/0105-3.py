while True :
    score = int(input('점수를 입력하세요 : '))
    if score > 100 or score < 0 :
        print('잘못 입력하셨습니다.')
        break
    if score >= 90 :
        grade = 'A'
    elif score >= 80 :
        grade = 'B'
    else :
        grade = 'C'
    print('학점은 %s 입니다.' %(grade))
