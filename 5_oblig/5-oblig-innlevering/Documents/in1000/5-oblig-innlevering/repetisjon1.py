"""
Programmet ber om ord som legges til i en liste og kan skrives ut.
"""

mineOrd = ['Per', 'er', 'rar']

def slaaSammen(x,y):
    return x + y

print(slaaSammen("slaa", "Sammen"))

def skrivUt(liste):
    # skriv ut hvert ord til terminalen.
    for x in liste:
        print(x)

    # Python vil alltid returnere fra en funksjon/prosedyre
    # så for å hindre at 'None' blir printet så returnerer vi en tom string.
    # Jeg vet at det blir bedt om en prosedyre, men det er ingen som holder styr på det.
    # De to konseptene skaper bare forvirring - i alle fall for meg
    return ""

# Skriv ut listen med ord på hver sin linje med en 'for' løkke
print(skrivUt(mineOrd))

def skrivUt2(liste):
    """
    Alternativ utskriftsfunksjon som skriver ut en liste med mellomrom mellom hvert element
    """
    return (" ".join(liste))

# While løkke som ber om input på hva brukeren vil gjøre
inn = "i"
while inn == 'i' or inn == 'u':
    print("'i' for input av ord; 'u' for utskrift av ordene; eller 's' for stopp: ")
    inn = input("'i', 'u' eller 's': ")

    if inn == "i":
        ord = input("Skriv et ord:")
        mineOrd.append(ord)

    elif inn == "u":
        print(skrivUt2(mineOrd))
       #print(" ".join(mineOrd))

    elif inn == "s":
        print("Good bye!")
        # break

    else:
        print("Programmet avsluttes siden valget ikke var 'i' eller 'u'.")
