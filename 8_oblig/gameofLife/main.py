from spillebrett import Spillebrett# as S

def main():

    rader = int(input("Hvor mange rader vil du ha? "))
    kolonner = int(input("Hvor mange kolonner vil du ha? "))

    # Opprett instansen av brettet
    brett = Spillebrett(rader, kolonner)
    # Tegn ut brettet
    brett.tegnBrett()
    print()
    # Sett while loop control variable
    new_generation = ""
    print(f"Det er nå {brett.finnAntallLevende()} levende celler.")
    print("Vil du se en generasjon til?")

    while new_generation != "q":
        try:
            # Spør om hva bruker vil
            new_generation = input("Press 'Enter' or 'q' to quit. ")
            # Sjekk om bruker vil se en ny runde ved å trykke enter
            if new_generation == "":
                brett.oppdatering()
                brett.tegnBrett()

        except expression as identifier:
            print("Feil valg - You STUPID!")
        # Hvis noe annet enn 'Enter' eller 'q' trykkes så går loopen en runde til uten å oppdatere.
        else:
            continue
        finally:
            print("Takk for nå.")



if __name__ == "__main__":
    main()