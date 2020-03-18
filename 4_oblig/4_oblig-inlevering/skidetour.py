""" Programmet holder rede på resultater for deltakere i et sett med skirenn.
En tour har 2 renn. første og andre.
Hvert renn har x(3) antall deltakere. Per, Pål og Espen.
Deltakere har en tid for hvert renn.
Tidene gir en plassering i rennet. """

# Liste med data om resultater(muligens litt klønete datamodell).
deltakere = [
              {"navn": "Per", "renn": [("første", 3768),("andre", 2736)]},
              {"navn": "Pål", "renn": [("første", 4132),("andre", 3567)]},
              {"navn": "Espen","renn": [("første", 4654),("andre", 4456)]}
              ]

# Print deltakerliste
print("Disse er med:")
for deltaker in deltakere:
  print(deltaker["navn"])

# Be om deltaker for operasjon 
person = input("Hvem lurer du på? ")

def finnDeltaker(person):
  for deltaker in deltakere:
    if person in deltaker["navn"]:
      return deltaker["renn"]
  # Hvis deltaker ikke finnes gis det beskjed. 
  # TODO Desverre får man da også en feilmelding og programmet crasher.
  print("Fant ikke deltaker.")  

# Funksjon som lager variabler med timer, minutter og sekunder av tiden og returnerer en tuple med 3 Heltall.
def formatTime(tid):
  hours = tid // 3600
  minutes = (tid - hours * 3600) // 60
  seconds = (tid - hours * 3600 - minutes * 60)
  return hours, minutes, seconds

# Funkjon som tar tekststrengen fra 'formatTime1 og legger til informasjon om  person og renn.
def printTime(person, renn, tid):
  # Sender tiden i sekunder til 'FormatTime som sender tilbake en tuple med heltall.
  x = formatTime(tid)
  
  print(f"Tiden for {person} i {renn} renn er: {x[0]} hour{'' if x[0] == 1 else 's'}, {x[1]} minutes, and {x[2]} seconds.")

# To kall til 'printTime() for å starte funksjonene med data om deltaker.
printTime(person, finnDeltaker(person)[0][0], finnDeltaker(person)[0][1])
printTime(person, finnDeltaker(person)[1][0], finnDeltaker(person)[1][1])

# Loop som ber om input om et renn som du kan få fesultatlisten for. Setter variablen x til '0' eller '1'.
# For å sikre at enten 'første' eller 'andre' er det som angis er det en while loop som ber om denne input. 
x = -1
while x != 0 or 1:
  renn = input("Hvilket renn vil du ha resultatlisten for('første' eller 'andre')?  ")
  if renn == "første":
    x = 0
    break
  if renn == "andre":
    x = 1
    break

# Funksjon som angir hvilken atributt data skal sorteres på i henhold til hvilket renn som angis av bruker.
# Vet ikke helt hvordan det virker, men det virker:-)
def myFunk(e):
  return e['renn'][x]

# Kall som sorterer data i henhold til definert 'key'
deltakere.sort(key=myFunk)

# Bygg en liste med informasjon om navn, tid og plassering
rennResultater2 = []
# Loop som lager 3 'arrays' med informasjon om deltakerne
for index, deltaker in enumerate(deltakere):

  # Siden data allerede er sotert på tid på valgt renn kan vi lage en plasseringsindex fra 'enumerate()'
  rennResultat = [index + 1, deltakere[index]["navn"],formatTime(deltakere[index]["renn"][x][1])]
  
  # For at tiden skal vises på format 'tt:mm:ss' formaterer vi siste datapunkt i listen
  rennResultat[2] = f"{rennResultat[2][0]:02d}:{rennResultat[2][1]:02d}:{rennResultat[2][2]:02}"

  # Hver liste den enkelte deltaker legges til 'rennResultater'-listen 
  rennResultater2.append(rennResultat)

# Skriv ut en overskrift for å vise hvilket renn dette er.
print("Første renn:") if x == 0 else print("Andre renn:")

# Print ut en tabell med resultatene.
for i in rennResultater2:
  print(f"{i[0]:<6}  |  {i[1]:<16}|  {i[2]:<16}")