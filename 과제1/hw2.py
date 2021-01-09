score_list = [] # 점수들을 저장하기 위한 리스트
score_sum = 0   # 점수의 총합

while True :
    score = input('점수를 입력하세요: ')

    if score == 'Quit' :    # Quit을 입력받으면 while문을 빠져나옴
        break
    score_list.append(int(score))   # 그렇지 않으면 리스트에 값을 추가함

if len(score_list) == 0 :   # 입력받은 점수가 없다면 계산을 하지 않음
    print('입력된 점수가 없습니다.')
else :  # 입력받은 점수가 있는 경우
    for i in range(len(score_list)) :   # 총합 계산
        score_sum += score_list[i]
        
    score_avg = score_sum / len(score_list) # 평균 계산

    if score_avg >= 90 :    # 학점 계산
        grade = 'A'
    elif score_avg >= 80 :
        grade = 'B'
    else :
        grade = 'C'
        
    print("입력된 점수의 총합은 %d점이고, 평균은 %.2f점입니다. 학점은 '%s'입니다." %(score_sum, score_avg, grade))   # 결과 출력

