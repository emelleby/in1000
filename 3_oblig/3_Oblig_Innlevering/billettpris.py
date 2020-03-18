# Pris funksjon
""" 
Programmet regner ut billettprisen for en bruker som angir sin alder i terminalen.
 """
def pris():
    # Ask for age
    alder = int(input("Hva er din alder?"))
    billettpris = 0

    # if age is less than or equal to 17 
    if(alder <= 17):
        billettpris = 30
        return billettpris

    # if age is between 17 and 63
    elif (17 < alder < 63):
        billettpris = 50
        return billettpris

    # if age is 63 or more
    else:
        billettpris = 35
        return billettpris
    
# Running function 4 times
print(pris())
print(pris())
print(pris())
print(pris())

# Skriver man inn alder med bokstaver så får man feilmelding
# Skriver man inn alder med flyttall så får man feilmelding
# Skriver man inn et negativt tall så får man barnepris.