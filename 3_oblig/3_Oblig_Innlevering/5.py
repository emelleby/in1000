""" Kommentarer er en blanding av oppgavetekst, psuedo-kode og kodekommentarer.
    Jeg håper det er greit slik som dette. 
    Programmet er en system for deltakeradministrasjon hvor man kan melde på og registrere 
    om de har betalt startavgift eller ei. Deltakere kan også slettes. :-) """


# Lag en liste over påmeldte til et skirenn og om de har betalt påmeldingsavgiften eller ikke.
paameldte = {
    'Ola': True,
    'Per': False,
    'Kari': True,
    'Espen': False
}

# Make sure the user enters a number (integer)
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Velg et tall mellom 1 -5. Prøv igjen: ")
       continue
    else:
       return userInput 
       break 
     
run = True
# Loop to run the program until terminated by user
while run == True:

    # Spør brukeren om de vil melde på en deltaker eller registere betalt avgift eller vise listen.
    print("")
    print("Melde på deltaker - tast 1")
    print("Registere om avgift er betalt - tast 2")
    print("Vise listen over påmeldte - tast 3")
    print("Slette deltaker - tast 4")
    print("Avslutte programmet - tast 5")

    # Spør hva brukeren vil
    valg = inputNumber("Hva vil du? ")

    # Hvis  de vil melde på en deltaker taster de inn 1
    if valg == 1:
    #   Be om navn
        navn = input("Navn på deltaker: ")
        print(navn + " navn")
        #   BETALT AVGIFTEN? JA/Nei
        betalt_input = input("Betalt avgift? Ja eller nei? ")
        if (betalt_input.lower() == "ja"):
            paameldte[navn] = True
        
        else:
            paameldte[navn] = False        
        # Gi tilbakemelding om at deltaker er påmeldt og betalingsstatus.
        print(navn + " er nå påmeldt. Status på betalingen er: " + str(paameldte[navn]))
        for deltaker, betalt in paameldte.items():
            print("{:<12} | Betalt: {}".format(deltaker, betalt))

    # Hvis de vil registere avgift taster de 2
    elif valg == 2:   
        #   Be om navn
        deltaker = input("Hvem vil du registrere som betalt? ")
        # REgistrer betalingen
        if deltaker in paameldte:
            paameldte[deltaker] = True
            print("Nå har {} betalingsstatus: {}".format(deltaker, paameldte[deltaker]))

        else:
            # Hvis deltaker navn ikke finnes gi beskjed og lis opp deltakere
            print("Fant bare disse deltakerne: ")
            for deltaker, betalt in paameldte.items():
                print("{:<12} | Betalt: {}".format(deltaker, betalt))

    # Hvis de vil skrive ut listen taster de 3
    elif valg == 3:
        for deltaker, betalt in paameldte.items():
            print("{:<12} | Betalt: {}".format(deltaker, betalt))
        
    # Vil du slette en deltager taster de 4
    elif valg == 4:
        # Skriv ut listen
        for deltaker, betalt in paameldte.items():
            print("{:<12} | Betalt: {}".format(deltaker, betalt))
        #   Be om navn
        deltaker = input("Hvem vil du slette fra listen? ")
        if deltaker in paameldte:
            # Slett deltaker fra listen
            del paameldte[deltaker]
        else:
            print("Finner ikke deltaker. Gjør et annet valg: ")
            continue
        # Skriv ut listen
        for deltaker, betalt in paameldte.items():
            print("{:<12} | Betalt: {}".format(deltaker, betalt))

    # stop while loop og avslutt programmet
    elif valg == 5:
        run = False
        break
    # Spør igjen om et nummer som er gyldig.
    else:
        valg = int(input("Velg mellom 1 - 5: "))

# Bekreft at programmet er avsluttet
print("Good bye!")


