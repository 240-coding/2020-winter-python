from temperature import convert_to_cel as convert

temp = float(input('화씨 온도를 입력하세요 : '))
cel = str(convert(temp))
print('섭씨 온도는 ' + cel + '입니다')
