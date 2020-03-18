"""
Programmet har en ordbok med nøkkel/navn på produkt og tilhørende verdi/pris. Ordboken skrives ut.
Programmet ber så om navn og pris på to varer og skriver ut ordboken på nytt.
"""

# Declare a dictionary with some values
prisliste = {"melk": 14.90, "brød": 24.90, "yogurt": 12.90, "pizza": 39.90}
print(prisliste)

# Get input for a product
x = input("Varenavn: ")
y = float(input ("Varepris: " ))

#Get input for a second product
x2 = input("Varenavn: ")
y2 = float(input ("Varepris: " ))

# Add the products to the dictionary
prisliste[x] = y
prisliste[x2] = y2

print(prisliste)