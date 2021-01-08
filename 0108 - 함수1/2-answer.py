def average() :
    score1 = int(input('점수를 입력하세요 : '))
    if score1 < 0 or score1 > 100 :
        print('잘못된 입력입니다.')
        return
    score2 = int(input('점수를 입력하세요 : '))
    if score2 < 0 or score2> 100 :
        print('잘못된 입력입니다.')
        return
    return (score1 + score2) / 2
    
