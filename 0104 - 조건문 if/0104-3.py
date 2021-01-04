pH = float(input('pH농도 입력 : '))

if pH > 7.0 :
    print("염기성")
elif pH < 7.0 :
    print("산성")
    if (pH < 3.0) :
        print("주의! 강산성")
else :
    print("중성")
