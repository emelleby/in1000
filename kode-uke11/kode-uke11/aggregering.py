
class Flyplass:
    """
    Klasse for å representere en flyplass
    og alle flyselskap som flyr herfra.

    Metoder:
        leggTilSelskap: parametre: selskap
        skrivAlleReisemaal: parametre: ingen
    """

    def __init__(self, navn):
        self._navn = navn
        self._flyselskap = []

    def leggTilSelskap(self, selskap):
        self._flyselskap.append(selskap)

    def skrivAlleReisemaal(self):
        for selskap in self._flyselskap:
            selskap.skrivReisemaalForSelskap()

    def leggTilLandForSelskap(self, selskap, land):
        selskap.leggTilLand(land)

    def leggTilReisemaalForSelskap(self, selskap, land, bynavn):
        selskap.leggTilByForLand(land, bynavn)

class Flyselskap:

    def __init__(self, navn):
        self._navn = navn
        self._reiseland = []

    def leggTilLand(self, land):
        self._reiseland.append(land)

    def leggTilByForLand(self, land, by):
        land.leggTilBy(by)

    def skrivReisemaalForSelskap(self):
        for land in self._reiseland:
            land.skrivByer()

class Land:

    def __init__(self, navn):
        self._navn = navn
        self._byer = []

    def leggTilBy(self, by):
        self._byer.append(by)

    def skrivByer(self):
        for by in self._byer:
            print(by)

    def hentByer(self):
        return self._byer


def enhetstest_land():
    testland = Land("Test")
    testland.leggTilBy("Hovedstaden")
    testland.skrivByer()

def enhetstest_flyselskap():
    selskap = Flyselskap("TestFly")
    landet = Land("Testland")
    selskap.leggTilLand(landet)
    selskap.leggTilByForLand(landet, "Testby")
    selskap.skrivReisemaalForSelskap()

def kjoer_enhetstester():
    enhetstest_land()
    print("Enhetstest for land OK")
    enhetstest_flyselskap()
    print("Enhetstest for flyselskap OK")

def hovedprogram():
    gardermoen = Flyplass("Gardermoen")
    sas = Flyselskap("SAS")
    norge = Land("Norge")

    gardermoen.leggTilSelskap(sas)
    gardermoen.leggTilLandForSelskap(sas, norge)
    gardermoen.leggTilReisemaalForSelskap(sas, norge, "Bergen")
    gardermoen.leggTilReisemaalForSelskap(sas, norge, "Trondheim")
    gardermoen.skrivAlleReisemaal()

kjoer_enhetstester()
hovedprogram()
