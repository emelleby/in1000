from celle import Celle# as C
import random

class Spillebrett:
    """ 
    classen Spillebrett tar et antall rader og kolonner som parameter.
    classen har en nøstet løkke som attributt som holder på celle instanser
    """
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._gen = 0

        # Lag en nøstet liste
        self._brett = []

        # Populer spillebrettet/listen med instanser av celler
        for rad in range(self._rader):
            rad = []
            for celle in range(self._kolonner):
                rad.append(Celle())
            self._brett.append(rad)
        # Call _generer for å sette status på cellene
        # Jeg kan vel kanskje kalle på _generer over og sette status direkte på en måte?
        self._generer()

    def tegnBrett(self):
        """ tegnBrett skriver Spillebrettet ut til terminalen med tegn iht status"""
        for rad in self._brett:
            for celle in rad:
                print(celle.hentStatusTegn(), end='')
            print("\n")
        print(f"Dette er generasjon {self._gen}")
            
    def oppdatering(self):
        """
        oppdatering() kjører en oppdateringsrutine som lager to lister hvor alle objektene 
        deles inn iht status for neste generasjon
        """
        levende = []
        doed = []
        celler = 0
        totalt = 0
        # Finn ut hvilken status hver celle skal ha i neste generasjon
        # for hver celle
        for x, rad in enumerate(self._brett):
            for y, celle in enumerate(rad):
                totalt += 1
                # Hvor mange av cellens naboer lever?
                naboer = (self.finnNabo(x, y))
                alive = 0
                dead = 0
                for nabo in naboer:
                    if nabo.erLevende():
                        alive += 1
    
                    else:
                        dead += 1
                
                if celle.erLevende():
                    # Hvis cellen har to eller tre levende naboceller vil cellen leve
                    if alive == 2 or alive == 3:
                        levende.append(celle)
                        celler += 1

                    # Ellers vil den dø
                    else:
                        doed.append(celle)
                        celler += 1
                
                if not celle.erLevende():

                    if alive == 3:
                        levende.append(celle)
                        celler += 1
                        print("død celle blir levende")
                    else:
                        doed.append(celle)
                        celler += 1

        print(len(self._brett))
        print(totalt)
        print("celler:" + str(celler))
        print("levende:" + str(len(levende)))
        print("Døde:" + str(len(doed)))
        # Selve oppdateringen
        for rad in self._brett:
            for celle in rad:
                # Will a use of a try-except block be useful here?
                if celle in levende:
                    celle.settLevende()
                
                elif celle in doed:
                    celle.settDoed()

                else:
                    print("Error i oppdatering.")
        # Oppdater generasjonsvariablen
        self._gen += 1
        
    def finnAntallLevende(self):
        tall = 0
        for rad in self._brett:
            for celle in rad:
                # tell alle celler som lever
                if celle.erLevende():
                    tall += 1
        return tall
    
    def _generer(self):
        for rad in self._brett:
            for celle in rad:
                tall = random.randint(0,2)
                if tall == 0:
                    celle.settLevende()
                else:
                    celle.settDoed()


    
    def finnNabo(self, cellerad, cellekolonne):
        """
        finnNabo() tar en celles indexaddresse i form av rad og kolonne som input
        funksjonen leveer en liste med alle celler(objekter) som er nabo til cellen(self)
        """
        # definer søkeområdet
        sok_min = -1
        sok_max = 2

        naboliste = []

        # sjekk naboer start med -1, - opp til 2
        # start med første rad i matrisen
        for rad in range(sok_min, sok_max ):
            # start med første kolonne på den raden og ta en og en celle bortover
            for kolonne in range(sok_min, sok_max ):
                naborad = rad + cellerad
                nabokolonne = kolonne + cellekolonne

                # Sjekk om nabocellen er utenfor matrisen (North, West, East, South)
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