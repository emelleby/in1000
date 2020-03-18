def les_datoverdier(filnavn):
	datoverdier = {}
	for linje in open(filnavn):
		biter = linje.split()
		dato = biter[0]
		regn = float(biter[1])
		datoverdier[dato] = regn
	return  datoverdier

dagsregn = les_datoverdier("regn.csv")
dagssok = les_datoverdier("trends.csv")

sum_dorlig_ver = 0
sum_bra_ver = 0
antall_dager_dorlig = 0
antall_dager_bra = 0

assert dagsregn.keys() == dagssok.keys()
datoer = dagsregn.keys()

for dato in datoer:
	if dagsregn[dato] >2:
		sum_dorlig_ver += dagssok[dato]
		antall_dager_dorlig += 1
	else:
		sum_bra_ver += dagssok[dato]
		antall_dager_bra += 1

print("Gjennomsnittlig score dager med bra ver:")
print( sum_bra_ver / antall_dager_dorlig )
print("Gjennomsnittlig score dager med daarlig ver:")
print( sum_dorlig_ver / antall_dager_bra )
