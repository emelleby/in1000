from celle import Celle as C
import random

class Spillebrett:

    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._gen = 0

        # lag en nøstet liste
        self._brett = []

        # Populer spillebrettet med instanser av celler
        for rad in range(self._rader):
            rad = []
            for celle in range(self._kolonner):
                rad.append(C())
            self._brett.append(rad)
        
        self._generer()

    def tegnBrett(self):
        for rad in self._brett:
            for celle in rad:
                print(celle.hentStatusTegn(), end='')
            print("\n")
    
    def oppdatering(self):
        levende = []
        doed = []

        # Finn ut hvilken status hver celle skal ha i neste generasjon
        # for hver celle
        for x, rad in enumerate(self._brett):
            for y, celle in enumerate(rad):
                # Hvor mange av cellens naboer lever?
                naboer = (self.finnNabo(x, y))
                # print(naboer)
                alive = 0
                dead = 0
                for nabo in naboer:
                    if nabo._alive:
                        alive += 1
    
                    else:
                        dead += 1

                # Hvis cellen har to eller tre levende naboceller vil cellen leve
                if alive == 2 or alive == 3:
                    # celle.settLevende()
                    # self._alive = True
                    #print(alive)
                    #print("Alive")
                    levende.append(celle)

                # Ellers vil den dø
                else:
                    # celle.settDoed()
                    # self._alive = False
                    doed.append(celle)
        print(len(levende))
        # print(doed)
        # Selve oppdateringen
        for rad in self._brett:
            for celle in rad:
                # Will a use of a try-except block be useful here?
                if celle in levende:
                    celle._alive = True
                    # print("Yes")

                elif celle in doed:
                    #print("No")
                    celle._alive = False

                else:
                    print("Error i oppdatering.")
        

        self._gen += 1
        
    
    def finnAntallLevende(self):
        tall = 0
        for rad in self._brett:
            for celle in rad:
                # tell alle celler som lever
                if celle._alive:
                    tall += 1
    
    def _generer(self):
        for rad in self._brett:
            for celle in rad:
                tall = random.randint(0,2)
                if tall == 0:
                    celle._alive = True
                else:
                    celle._alive = False


    
    def finnNabo(self, cellerad, cellekolonne):
        # definer søkeområdet
        search_min = -1
        search_max = 2

        naboliste = []

        # sjekk naboer start med -1, -1 - Hvis det er 'E' så vil det være 'A'
        # start med første rad i matrisen
        for rad in range(search_min, search_max):
            # start med første kolonne på den raden og ta en og en celle bortover
            for kolonne in range(search_min, search_max):
                naborad = rad + cellerad
                nabokolonne = kolonne + cellekolonne

                # Sjekk om nabocellen er utenfor matrisen (North,West, East, South)
                if naborad < 0:
                    continue
                if nabokolonne < 0:
                    continue
                if nabokolonne >= len(self._brett[0]):
                    continue
                if naborad >= len(self._brett):
                    continue

                # Sjekk om cellen er sin egen
                elif naborad == cellerad and nabokolonne == cellekolonne:
                    continue
                
                # Ellers legges cellen til nabolisten
                else:
                    naboliste.append(self._brett[naborad][nabokolonne])

        return naboliste