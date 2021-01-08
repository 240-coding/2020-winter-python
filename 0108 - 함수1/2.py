def average() :
    score1 = int(input('점수를 입력하세요 : '))
    score2 = int(input('점수를 입력하세요 : '))
    
    if score1 < 0 or score1 > 100 or score2 < 0 or score2 > 100 :
        print('잘못된 점수입니다.')
    else :
        return ((score1 + score2) / 2)
    
