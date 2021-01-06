elements = ['Li', 'Na', 'K', 'F', 'Cl']

i = len(elements) - 1
value = input('탐색할 원소를 입력하세요 : ')

while i >= 0 and elements[i] != value :
    i = i - 1

if i < 0 :
    print('탐색 실패 - 원소가 존재하지 않습니다.')
else :
    print('원소 %s는 %d 번째에 존재합니다.' %(value, i))
