# Lister til lagring av datainput
steder =[]
klesplagg = []
avreisedatoer = []

# Hent inn data til reiseplanen og legg informasjonen inn i de tre listene.
for i in range(2):
    steder.append(input("Reisemål " + str(i + 1) + ": "))
    klesplagg.append(input("Klesplagg " + str(i + 1) + ": "))
    avreisedatoer.append(input("avreisedatoer " + str(i + 1) + ": "))

# Opprett reiseplan 
reiseplan = []

# Nøst listene inn i listen 'reiseplan' som tre data
reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedatoer)

# Print ut reiseplanen
for i in range(len(reiseplan)):
    print(reiseplan[i])

# Lag en liten tabell
# Lag overskrifter( Dette virker litt vel komplisert)
# Lag en ny liste først i reiseplanen med samme lengde som lister som er der
x = "Reisemål"
y = 1
# Opprett listen og første 'record 
reiseplan.insert(0, [x + ' ' + str(y)])

# Legg til så mange som trengs for å få en til hver kolonne
while y < len(reiseplan[1]):
    reiseplan[0].insert(1, x + ' ' + str(y + 1))
    y += 1
    
print(reiseplan)
# Skriv ut reiseplanen oversiktlig.
for i in reiseplan:
  for reise in i:
    
    print(f"{reise:<10}", end = ' | ')

  print("")

# Valider om input er Heltall (Denne bruker en 'while true' som kanskje ikke er helt innafor. Ideer?)
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Må være heltall. Prøv igjen.")
       continue
    else:
       return userInput 

x = 0
while x == 0:
    # Få input om ønsket 'item' i den nøstede listen.
    i1 = int(inputNumber("i1: "))
    i2 = int(inputNumber("i2: "))

    # Sjekk om input er lik eller større enn '0' og om det er innenfor lengden til listene.
    if 0 <= i1 < len(reiseplan) and 0 <= i2 < len(reiseplan[0]):
        print(reiseplan[i1][i2])
        x == 1
        break
    else:
        print("Ugyldig")
        x == 0