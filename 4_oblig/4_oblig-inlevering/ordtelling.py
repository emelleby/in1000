# Funksjon som teller bokstaver i en streng
# tekst = input("Gi meg et ord å telle: ")
def tell(tekst):
  return len(tekst)

# Funksjon som tar en setning som input og returnerer en ordliste som har ordene som nøkkel og antall ganger som verdi
def setningTilOrdbok():
# Be om en setning fra brukeren
  setning = input("Skriv en setning: ")
  # Del setningen opp i ord og lagre i listen
  ordList = setning.split()
  # Skriv ut hvor mange ord setningen har.
  print(f"Setningen har {len(ordList)} ord.")
  # Definer en ordliste
  ordliste = {}

  # For hvert ord i listen(ordList) opprett en nøkkel i ordlisten og sett antall ganger ordet er med som verdi
  for ord in ordList:
    ordliste[ord] = ordList.count(ord)
  return ordliste

# Funksjon som henter en Dict fra 'setningTilOrdbok()' og skriver ut infomasjon om setningen.
def printOut():
  ordliste = setningTilOrdbok()
  
  # Loop som skriver ut data om hvert ord i ordlisten.
  for key, value in ordliste.items():
    print(f"Ordet '{key}' forekommer {value} gang{'' if value==1 else 'er'} og har {tell(key)} bokstav{'' if len(key)==1 else 'er'}.")

# Funksjonskall som starter programmet.
printOut()