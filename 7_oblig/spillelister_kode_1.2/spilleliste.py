#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:13:54 2020

@author: eivind
"""

from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn
        
    def __str__(self):
        print(f"Spillelisten {self._navn} inneholder:")
        string = []
        for sang in self._sanger:
            string.append(str(sang))
            
        return '\n'.join(string)
        # return f"{self._navn}:\n {for sang in self._sanger: print(f'Nå spilles følgende: {sang}')}"
        
        
    def lesFraFil(self, filnavn):
        """
        Metoden som tar en fil med 2 verdier separert med semikolon som parameter.
        og legger linjene in i en ordbok.
        
        Ordboken returneres
        """                
        self._sanger.clear()
 
        # Les en fil med musikk
        innfil = open(filnavn, mode='r')
        
            
        for i, linje in enumerate(innfil):
            biter = linje.strip().split(';')
            # sang = "sang" + str(i+1)
            # Opprett et objekt for hver sang
            # print(sang)
            sang = Sang(biter[0], biter[1])
            
            # Legg objektet(sangen) til i spillelisten
            self._sanger.append(sang)
            
        # Lukk filen
        innfil.close()
        # print(self._sanger)
        # print(allMusikk) NO
        print()
    
    def spillAlle(self):
        """ 
        Metoden spiller alle sangene i spillelisten
        """
        for sang in self._sanger:
            print(f"Nå spilles følgende: {sang}")
            
    def leggTilSang(self, nySang):
        """ Metoden legger til et objekt til listen av sanger i spillelisten """
        self._sanger.append(nySang)
        
    def spillSang(self, sang):
        print(f"Nå spilles følgende: {sang}")
        
    def finnSang(self, tittel):
        for sang in self._sanger:
            if sang._tittel == tittel:
                return sang
            
    def hentArtistUtvalg(self, artistnavn):
        sangliste = []
        for sang in self._sanger:
            # print(sang._artistList)
            if artistnavn in sang._artistList:
                sangliste.append(sang)
                #print(sang)
                #print(sangliste)
        return sangliste
        # return [sang for sang in self._sanger if sang._artist == artistnavn]
        #print(sangliste)
        #return sangliste
        
    def fjernSang(self, sang):
        """ Metoden fjerner en sang fra spillelisten """
        self._sanger.remove(sang)
        
        



def main():
    Spilleliste.lesFraFil("musikk.txt")
    #print(Spilleliste.)



if __name__ == "__main__":
    
    main()
    
