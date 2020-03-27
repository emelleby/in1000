from celle import Celle as C

class Spillebrett:

    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._gen = 0

        # lag en nøstet liste
        self._brett = []

        for rad in range(self._rader):
            rad = []
            for kolonne in range(self._kolonner):
                rad.append(C())
            self._brett.append(rad)


    def tegnBrett(self):
        pass
    
    def oppdatering(self):

        self._gen += 1
        pass
    
    def finnAntallLevende(self):
        pass
    
    def _generer(self):
        pass
    
    def finnNabo(self, rad, kolonne):
        pass