hex = "0123456789abcdef"


def ConvertToHex(x) :
    q = x // 16
    r = x % 16

    if q == 0 :
        return hex[r]
    else :
        return ConvertToHex(q) + hex[r]


num = int(input('10진수 정수 입력 : '))
print(ConvertToHex(num))
    
    
    
