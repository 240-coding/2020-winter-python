for x in range(0, 5) :
    space = ''  # 빈칸을 출력하기 위한 변수
    stars = ''  # *를 출력하기 위한 변수
    for y in range(x+1, 5) :    # 빈칸은 1개로 시작해서 하나씩 늘어남
        space += ' '
    for z in range(0, 2*x+1) :  # *는 1개로 시작해서 2개씩 늘어남
        stars += '*'
    print('%s%s' %(space, stars))   # 빈칸과 * 함께 출
