
class Flyplass:

    def __init__(self, navn):
        self._navn = navn
        self._flyselskap = []

    def leggTilSelskap(self, selskap):
        self._flyselskap.append(selskap)

    def skrivAlleReisemaal(self):
        for selskap in self._flyselskap:
            for land in selskap._reiseland:
                for by in land._byer:
                    print(by)

    def leggTilLandForSelskap(self, selskap, land):
        for s in self._flyselskap:
            if s == selskap:
                selskap._reiseland.append(land)

    def leggTilReisemaalForSelskap(self, selskap, land, bynavn):
        for s in self._flyselskap:
            if s == selskap:
                for l in s._reiseland:
                    if l == land:
                        l._byer.append(bynavn)

class Flyselskap:

    def __init__(self, navn):
        self._navn = navn
        self._reiseland = []

class Land:

    def __init__(self, navn):
        self._navn = navn
        self._byer = []


def hovedprogram():
    gardermoen = Flyplass("Gardermoen")
    sas = Flyselskap("SAS")
    norge = Land("Norge")

    gardermoen.leggTilSelskap(sas)
    gardermoen.leggTilLandForSelskap(sas, norge)
    gardermoen.leggTilReisemaalForSelskap(sas, norge, "Bergen")
    gardermoen.leggTilReisemaalForSelskap(sas, norge, "Trondheim")
    gardermoen.skrivAlleReisemaal()

hovedprogram()
