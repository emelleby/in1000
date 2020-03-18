"""
Programmet legger sammen, trekker fra, og deler tall.
Det kan også bergne antall cm når det vet antall tommer.
"""


def addisjon(x,y):
    """
    Function to add two aguments
    """
    return x+y

assert addisjon(3, 4) == 7
assert addisjon(-3, -2) == -5
assert addisjon(4, -2) == 2

print(addisjon(3,4))

def subtraksjon(x,y):
    """
    Function to subtract second agument from first
    the rounded result is returned
    """
    return round(x-y,2)

assert subtraksjon(3, 4) == -1
assert subtraksjon(-3, -2) == -1
assert subtraksjon(-3, 2) == -5
# assert subtraksjon(2.4, 2.1) == 0.30

print(f"{subtraksjon(12,8):.2f}")
# print(subtraksjon(2.4, 2.1))

def divisjon(x,y):
    """
    Function to devide first agument with the second
    the rounded result is returned
    """
    return round(x/y, 2)

assert divisjon(3, 4) == 0.75, "right"
assert divisjon(-3, -2) == 1.5
assert divisjon(-4, 2) == -2

print(divisjon(3,4))

def tommerTilCm(tommer):
    """
    Function to convert inches to cm. It takes one argument
    the rounded result is returned with 2 decimals
    """
    assert tommer > 0
    return round(tommer * 2.54, 2)

print(tommerTilCm(28))


def skrivBeregninger():
    """
    Function to collect two numbers and add, subtract and devide them
    it will also ask for a number in inches to convert to cm.
    """
    print("Utregninger:")
    x = float(input("Skriv et tall 1: "))
    y = float(input("Skriv et tall 2: "))
    print("")
    print(f"Summen av tall 1 og 2 er: {addisjon(x,y)}")
    print(f"Resultatet av subtraksjon er: {subtraksjon(x,y)}")
    print(f"Resultatet av divisjonen er : {divisjon(x,y)}\n")

    tall = float(input("Skriv et tall i tommer: "))
    print(f"{tall} tommer i centimeter er: {tommerTilCm(tall)}cm.")

skrivBeregninger()
