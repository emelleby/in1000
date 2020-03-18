rliste = open("resultlist-2.csv", "r")

lineCount = 0
linjer = []
for linje in rliste:
    lineCount += 1
    biter = linje.split(';')
    linjer.append(biter)


print(linjer[1])
print(linjer[1][3])
print(lineCount)

#print(biter)


