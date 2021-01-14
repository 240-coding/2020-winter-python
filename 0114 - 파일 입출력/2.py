# w+ : 읽기 또는 쓰기 모드, 파일 없으면 새로 만든다.
file = open('color.txt', 'w+')
file.write('The color is brown')

file.seek(13)
file.write('green')

file.seek(0)

print(file.read())

file.close()
