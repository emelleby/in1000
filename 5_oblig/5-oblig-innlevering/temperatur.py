
temp = open("temperatur.txt", 'r+')
tempListe = []
for linje in temp:
    # print("Her fant jeg : " + linje)
    tempListe.append(linje)

print(tempListe)
tempListe2 =[]
for ele in tempListe:
    ele2 = ele.rstrip() 
    # assert ele2[-1] 
    tempListe2.append(ele2)
print(tempListe2)

 

def average(x):
    sum = 0
    for ele in x:
        sum += float(ele)
    return round(sum / len(x), 2)

assert average([6.6, 4, -1.6]) == 3
print(average(tempListe2))

temp.close()
