"""
Programmet skriver ut tall fra en liste i første omgang.
Deretter spør programmet etter fire navn som lagres i en liste.
Hvis et av navnene er 'Jose' så svarer det 'Du husket meg', hvis ikke så svarer det 'Glemte du meg'.
Til slutt skrives summen og produktet av den første listen ut i terminalen.
"""

# List with numbers
liste=[1,2,3]
liste.append(4)
print("Første tall i listen er: {} \nTredje tall i listen er: {}.".format(liste[0], liste[2]))

# Empty list for names
navn_liste = []

# Ask for input from user
for i in range(1,5):
    navn_liste.append(input("Navn " + str(i) + ": "))

#Check if name is in the list - Print message if it is or different if not.
if "Jose" in navn_liste:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

#New list for the sum and the product
sumProduktListe = []

#Add and add the sum to the list
sumProduktListe.append(sum(liste))

# Function to calculate the product of the numbers in the list
def produkt(liste):
    produkt = 1
    for i in liste:
        produkt *= i
    return produkt

# Recursive variant to calculate the product. Just for fun.
def produkt2(l, i):
    if i == 0:
        return l[i]
    return l[i] * produkt2(l, i - 1)

# Append the product to the list
sumProduktListe.append(produkt2(liste, len(liste) - 1))

print("Summen er : {}\nProduktet er : {}".format(sumProduktListe[0], sumProduktListe[1]))

