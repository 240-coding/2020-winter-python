elements = ['Li', 'Na', 'K', 'F', 'Cl']

i = -1
value = input('탐색할 원소를 입력하세요 : ')

while i != -len(elements)-1 and elements[i] != value :
    i = i - 1

if i == -len(elements) - 1 :
    print('탐색 실패 - 원소가 존재하지 않습니다')
else :
    print('원소 %s는 %d번째에 있습니다.' %(value, i))
