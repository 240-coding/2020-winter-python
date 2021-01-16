from temperature import convert_to_cel as convert

temp = float(input('조리 온도를 화씨로 입력하세요 : '))
cel = str(convert(temp))
print('오븐을 ' + cel + '도로 예열하세요')
