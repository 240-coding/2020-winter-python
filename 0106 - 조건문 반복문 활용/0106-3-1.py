elements = ['Li', 'Na', 'K', 'F', 'Cl']

value = input('탐색할 원소를 입력하세요 : ')

for i in range(len(elements) - 1, -1, -1) :
    if elements[i] == value :
        print('원소 %s는 %d 번째에 있습니다.' %(value, i))
        break

if i == 0 and elements[i] != value :
    print('탐색 실패 - 원소가 존재하지 않습니다.')
