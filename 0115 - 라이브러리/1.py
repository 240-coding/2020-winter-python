import random

while True:
    print(random.randint(1, 6))  # 모듈 내 속한 함수명 앞에 모듈 이름을 써줘야 함!!
    newGame = input('주사위를 다시 굴리겠습니까? ')

    if newGame == 'yes' or newGame == 'y':
        continue
    else:
        break
