dicKor = {'일': 'one', '이': '', '삼': 'three', '사': 'four', '오': 'five',
          '육': 'six', '칠': 'seven', '팔': 'eight', '구': 'nine', '십': 'ten'}
dicEng = {'one': '일', 'two': '이', 'three': '삼', 'four': '사', 'five': '오',
          'six': '육', 'seven': '칠', 'eight': '팔', 'nine': '구', 'ten': '십'}

num = input('단어를 입력하세요 : ')

if num in dicKor:
    print(dicKor[num])
elif num in dicEng:
    print(dicEng[num])
else:
    print('잘못 입력하셨습니다.')
