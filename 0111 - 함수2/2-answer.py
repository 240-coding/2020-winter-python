def average(score1, score2, score3, score4) :
    if score1 < 0 or score1 > 100 :
        print('Invalid parameter')
        return
    elif score2 < 0 or score2 > 100 :
        print('Invalid parameter')
        return
    elif score3 < 0 or score3 > 100 :
        print('Invalid parameter')
        return
    elif score4 < 0 or score4 > 100 :
        print('Invalid parameter')
        return

    score_list = [score1, score2, score3, score4]
    score_list.sort()
    score_list.reverse()

    sum = 0
    for i in range(0, 3) :
        sum += score_list[i]

    result = sum / 3
    return result
    
