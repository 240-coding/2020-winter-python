score = int(input('점수를 입력하세요 : '))

if score >= 60 :
    if score >= 70 :
        if score > = 80 :
            if score >= 90 :
                grade = 'A' # score 80 이상 & 90 이상
            else :
                grade = 'B' # 80 이상 & 90 미만
        else grade = 'C'    # 80 미만 & 70 이상
    else grade = 'D'        # 70 미만 & 60 이상
else :
    grade = 'F'             # 60 미만
    
print("학점은 %s 입니다" %(grade))
