mineOrd = ['Per', 'er', 'dum']

def slaaSammen(x,y):
    return x + y

print(slaaSammen("slaa", "Sammen"))

def skrivUt(liste):
    # skriv ut hvert ord til terminalen.
    for x in liste:
        print(x)

    # Python vil alltid returnere fra en funksjon så for å hindre at 'None' blir printet så returnerer vi en tom string.    
    return ""
print(skrivUt(mineOrd))

print(" ".join(mineOrd))


inn = "i"
while inn == 'i' or inn == 'u':
    print("'i' for input av ord; 'u' for utskrift av ordene; eller 's' for stopp: ")
    inn = input("'i', 'u' eller 's': ")
    if inn == "i":
        ord = input("Skriv et ord:")
        mineOrd.append(ord)
    elif inn == "u":
       print(" ".join(mineOrd))
       continue
    elif inn == "s":
        print("Good bye!")
        # break

    else:
        print("Programmet avsluttes siden valget ikke var 'i' eller 'u'.")

