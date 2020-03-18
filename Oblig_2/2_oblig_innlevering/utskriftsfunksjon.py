# prosedyre
def nameAndPlace():
    # Ask for input
    navn = input("Skriv inn ditt navn? ")

    # Ask for input
    bosted = input("Hvor kommer du fra? ")

    # Print out strings and variables
    print ("Hei " + str(navn) + "! Du er fra " + str(bosted) + ".")

# loop 3 times nameAndPlace()
i = 0  
while i < 3:
    nameAndPlace()
    i = i + 1
