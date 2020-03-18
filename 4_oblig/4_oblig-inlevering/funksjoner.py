"""
Programmet handler om funksjoner og returverdier. Det er funksjoner som legger sammen tall.
Og det er en funksjon som teller forekomst av bokstav i streng.
"""
# 1. Funksjon som legger sammen 2 tall
def adder(tall1,tall2):
    return tall1 + tall2

print("Resultatet er: " + str(adder(2,3)))

print("Resultatet av summeringen er {} hvis man legger sammen 2 og 4.".format(adder(2,4)))

# 2. Telling av bokstav i tekststreng
streng = input("Tekststreng, takk:")
bokstav = input("Bokstav, takk:")



# 3. Funksjon som teller bokstaver i streng
def tellForekomst(minTekst, minBokstav):
    return minTekst.count(minBokstav)

print(tellForekomst(streng, bokstav))