"""
Programmet leser inn en fil med temperaturer og beregner gjennomsnittet av disse.
"""
temp = open("temperatur.txt", 'r')
tempListe = []
for linje in temp:
    tempListe.append(linje)

# print(tempListe)

# Stripper bort 'newline char'
tempListe2 =[]
for ele in tempListe:
    ele2 = ele.rstrip()
    tempListe2.append(ele2)

# Skriver ut listen
print(tempListe2)

def average(x):
    """
    Function to calculate the average of a list of numbers provided as argument.
    """
    sum = 0
    for ele in x:
        sum += float(ele)

    # returnerer avrundet gjennomsnitt med 2 decimaler
    return round(sum / len(x), 2)

assert average([6.6, 4, -1.6]) == 3

# Skriver ut gjennomsnittet
print(f"Den gjennomsnittlige temperaturen er {average(tempListe2)} grader.")

# Lukker filen
temp.close()
