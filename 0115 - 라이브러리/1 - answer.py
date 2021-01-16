import random

def dice() :
    return random.randint(1, 6)

while True :
    print("주사위의 값 :" +str(dice()))
    cont = input("계속하시겠습니까(Y/N): ")

    if (cont.upper() == "Y" or cont.upper() == "YES") :
        continue
    else :
        break
