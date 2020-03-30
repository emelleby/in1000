from spillebrett import Spillebrett as S

def main():

    rader = int(input("Hvor mange rader vil du ha? "))
    kolonner = int(input("Hvor mange kolonner vil du ha? "))

    #Opprett instansen av brettet
    brett = S(rader, kolonner)
    #Tegn ut brettet
    S.tegnBrett(brett)
    print(f"Dette er generasjon {brett._gen}")
    print(f"Det er nå {brett.finnAntallLevende()} levende celler.")
    print("Vil du se en generasjon til?")
    new_generation = input("Press 'Enter' or 'q' to quit. ")

    while new_generation == "" and new_generation != "q":

        print()
        #print(new_generation + " enter")
        S.oppdatering(brett)

        S.tegnBrett(brett)

        print(f"Dette er generasjon {brett._gen}")
        print(f"Det er nå {brett.finnAntallLevende()} levende celler.")
        print("Vil du se en generasjon til?")

        new_generation = input("Press 'Enter' or 'q' to quit. ")
        


if __name__ == "__main__":
    main()