score = int(input('점수를 입력하세요 : '))

if score >= 90 :
    grade = 'A'
elif score >= 80 and score < 90 :
    grade = 'B'
elif score >= 70 and score < 80 :
    grade = 'C'
elif score >= 60 and score < 70 :
    grade = 'D'
else :
    grade = 'F'
    
print("학점 : %s" %(grade))
