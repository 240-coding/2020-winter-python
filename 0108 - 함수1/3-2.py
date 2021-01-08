oct = "01234567"


def ConvertToOct(x) :
    q = x // 8
    r = x % 8

    if q == 0 :
        return oct[r]
    else :
        return ConvertToOct(q) + oct[r]


num = int(input('10진수 정수 입력 : '))
print(ConvertToOct(num))
    
    
    
