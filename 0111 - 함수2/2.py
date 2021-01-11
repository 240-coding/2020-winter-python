def average(score1, score2, score3, score4) :
    score = [score1, score2, score3, score4]
    score.sort()

    result = (score[1] + score[2] + score[3]) / 3

    return result

score1 = int(input('첫번째 점수를 입력하세요 : '))
score2 = int(input('두번째 점수를 입력하세요 : '))
score3 = int(input('세번째 점수를 입력하세요 : '))
score4 = int(input('네번째 점수를 입력하세요 : '))

print('상위 세 점수의 평균 :', average(score1, score2, score3, score4))
