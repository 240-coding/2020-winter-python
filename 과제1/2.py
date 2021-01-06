score_list = []
score_sum = 0

while True :
    score = input('점수를 입력하세요: ')

    if score != 'Quit' :
        score_list.append(int(score))
    else :
        for i in range(len(score_list)) :
            score_sum += score_list[i]

        score_avg = score_sum / len(score_list)

        if score_avg >= 90 :
            grade = 'A'
        elif score_avg >= 80 :
            grade = 'B'
        else :
            grade = 'C'

        print("입력된 점수의 총합은 %d점이고, 평균은 %.2f점입니다. 학점은 '%s'입니다." %(score_sum, score_avg, grade))
        break
