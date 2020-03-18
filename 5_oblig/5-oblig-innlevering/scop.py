""" Selve oppgaven: ​Beskriv med ord hva som skjer når følgende program kjøres. 
Forsøk gjerne å løse oppgaven før du kjører programmet. """

def minFunksjon():
    # variablen x brukes ikke i denne funksjonen
    for x in range(2):
        c = 2

        # 2 Printes ut
        print(c)

        # c er nå lik 3
        c+=1

        b=10

        # Her blir det problemer. a er ikke definert i denne funksjonen
        b+=a
        print(b)
    return b

def hovedprogram():
    a=42
    b=0

    # Her printes 0
    print(b)

    # b settes lik 42 
    b=a

    a=minFunksjon()
    print(b)
    print(a)


# Her starter programmet   
hovedprogram()