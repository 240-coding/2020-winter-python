sum = 0
for x in range(0, 10) :
    if (x % 2 == 0) :
        continue
    sum += x
    print('Add', x)
print(sum)
