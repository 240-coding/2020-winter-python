for x in range(0, 5) :
    space = ''
    stars = ''
    for y in range(x+1, 5) :
        space += ' '
    for z in range(0, 2*(x+1)-1) :
        stars += '*'
    print('%s%s' %(space, stars))
