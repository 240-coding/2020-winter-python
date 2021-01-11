PI = 3.14159

def circle_area(x) :
    return PI * x * x

def circle_circumference(x) :
    return 2 * PI * x

r = float(input('반지름을 입력해주세요 : '))

print('원의 면적 :', circle_area(r))
print('원의 둘레 :', circle_circumference(r))
