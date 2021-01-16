def convert_to_cel(fah):
    return (fah - 32.0) * 5.0 / 9.0


if __name__ == "__main__":
    temp = float(input('화씨 온도를 입력하세요 : '))
    cel = str(convert_to_cel(temp))
    print('섭씨 온도는 ' + cel + '입니다')
