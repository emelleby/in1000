"""
Programmet har kontroll på hva beboere på et hjem skal spise. Bruker kan skrive inn et navn og så få
informasjon om hva vedkommende skal ha til de forskjellige måltidene.
"""

# Consistent preferences in food
mealplan ={
    "Kari": {"Frokost": "Grøt", "Lunsj": "Salat", "Middag": "Biff"},
    "Ola": {"Frokost": "Grøt", "Lunsj": "Salat", "Middag": "Biff"},
    "Per": {"Frokost": "Grøt", "Lunsj": "Salat", "Middag": "Biff"}
}

# Function to print mealplan
def mat():
    # Ask for name
    navn = input("Hvem vil du ha matplanen til?")

    # If name is in the plan
    if (navn in mealplan):
        print(navn + "s matplan: ")

        # iterate over the content of the mealplan and format the output
        for tid, mat in mealplan[navn].items():
            print("  {:<8}: {}".format(tid, mat))
    else:
        print("Finner ikke den beboeren.")

mat()

# a.Brukernavn på alle IN1000 studentene
""" Her ville jeg brukt en liste. Kan bruke mengde også siden alle vil være unike """
# b.Brukernavn og antall poeng på innlevering 3 for alle studentene på IN1000
""" Jeg ville brukt en ordbok/dict/objekt for den er lettere å utvide til å ha mer info om feks oblig 4
    Man kan vel også bruke en liste(eller array) som er nøstet """
# c.Alle vinnere i Lotto siste år (kun navn)
""" Her er en liste det som er mest nyttig. Index vil kunne representere ukenummer(-1) """
# d.All mat noen gjest i et selskap er allergisk mot (for å planlegge menyen)
""" Her er det nok mest hensiktsmessig å bruke en ordbok for å kunne få med all informasjonen,
    men en nøstet liste kan også gjøre jobben. """