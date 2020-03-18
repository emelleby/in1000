person = input("Konge: ")
etterkommere = {"Oscar":"Haakon", "Haakon":"Olav", "Olav":"Harald"}

barn = etterkommere[person]
barnebarn = etterkommere[barn]

print("Barnebarn: " + barnebarn)
