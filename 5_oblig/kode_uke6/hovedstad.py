hovedsteder = {}

for linje in open("hovedsteder.csv"):
    biter = linje.split()
    land = biter[0]
    by = biter[1]
    hovedsteder[land] = by

interesse = input("Hvilket land?: ")
print( hovedsteder[interesse] )
