from celle import Celle as C
import random

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
        
        self._generer()

    def tegnBrett(self):
        pass
    
    def oppdatering(self):

        self._gen += 1
        
    
    def finnAntallLevende(self):
        pass
    
    def _generer(self):
        for rad in self._brett:
            for celle in rad:
                tall = random.randint(0,2)
                if tall == 0:
                    celle._alive = True
                else:
                    celle._alive = False


    
    def finnNabo(self, rad, kolonne):
        pass