from spillebrett import Spillebrett# as S

def main():

    rader = int(input("Hvor mange rader vil du ha? "))
    kolonner = int(input("Hvor mange kolonner vil du ha? "))

    # Opprett instansen av brettet
    brett = Spillebrett(rader, kolonner)
    # Tegn ut brettet
    brett.tegnBrett()
    # Sett while loop control variable
    new_generation = ""

    while new_generation != "q":

        print()
        # Print info om generasjonen
        print(f"Dette er generasjon {brett._gen}")
        print(f"Det er nå {brett.finnAntallLevende()} levende celler.")
        print("Vil du se en generasjon til?")
        # Spør om hva bruker vil
        new_generation = input("Press 'Enter' or 'q' to quit. ")
        # Sjekk om bruker vil se en ny runde ved å trykke enter
        if new_generation == "":
            brett.oppdatering()
            brett.tegnBrett()
        # Hvis noe annet enn 'Enter' eller 'q' trykkes så går loopen en runde til uten å oppdatere.
        else:
            continue
        


if __name__ == "__main__":
    main()