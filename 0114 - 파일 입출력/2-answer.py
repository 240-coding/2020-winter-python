file = open('color.txt', 'w+')
file.write("The color is brown")

file.seek(13)
file.write("green")

file.seek(0)

print(file.read())

file.close()
