file = open('list.txt', 'r')
numList = []

for num in file:
    numList.append(int(num.strip()))

numList.sort()

file.close()

file = open('newList.txt', 'w+')

for i in range(len(numList)):
    file.write('0')
    file.write(str(numList[i]))
    file.write('\n')

file.seek(0)
print(file.read())

file.close()
