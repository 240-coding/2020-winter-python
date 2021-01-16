import temperature

temp = float(input('조리 온도를 화씨로 입력하세요: '))
cel = str(temperature.convert_to_cel(temp))
print('오븐을 섭씨 '+cel+'도로 예열하세요')
