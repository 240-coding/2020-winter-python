highest_score = 0
highest_name = ''

with open('example.txt', 'r', encoding = 'UTF8') as file :
    for line in file :
        current = line.split() # 한 줄씩 읽어온 후, 이름과 점수로 분리
        if int(current[1]) > highest_score :
            highest_score = int(current[1])
            highest_name = current[0]

print('가장 높은 성적 :', highest_score)
print('가장 높은 성적을 가진 학생 이름 :', highest_name)
