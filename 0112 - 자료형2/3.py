list = []
str = input('문자열을 입력하세요 : ')


def str_reverse(str):
    result = ''

    for i in range(len(str)):
        list.append(str[i])

    list.reverse()

    for i in range(len(list)):
        result += list[i]

    return result


print('결과 :', str_reverse(str))
