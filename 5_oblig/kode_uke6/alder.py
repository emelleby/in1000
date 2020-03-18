eldste_navn = "ingen"
maks_alder = 0
for linje in open("alder.csv"):
    biter = linje.split(":")
    navn = biter[0]
    alder = int(biter[1])
    if alder > maks_alder:
        maks_alder = alder
        eldste_navn = navn

print(eldste_navn)
