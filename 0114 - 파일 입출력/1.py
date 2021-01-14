# 파일에서 한글을 읽어올 때는 encoding = 'UTF8' 을 붙여줌
file = open('example.txt', 'r', encoding='UTF8')
highStudent = ''
highScore = 0
for line in file:
    if highScore < int(line.split()[1]):
        highStudent = line.split()[0]
        highScore = int(line.split()[1])

file.close()

print(highStudent, highScore)
