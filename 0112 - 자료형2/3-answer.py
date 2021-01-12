str = input('문자열을 입력하세요 : ')


def str_reverse(str):
    result = ''

    tempList = list(str)

    tempList.reverse()

    for i in range(len(tempList)):
        result += tempList[i]

    return result


print('결과 :', str_reverse(str))
