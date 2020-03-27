#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:13:54 2020

@author: eivind
"""

from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        """ Initialiserer en spilleliste og oppretter en liste til sanger """
        self._sanger = []
        self._navn = listenavn
        
    def __str__(self):
        print(f"Spillelisten {self._navn} inneholder:")
        string = []
        for sang in self._sanger:
            string.append(str(sang))
            
        return '\n'.join(string)
        
        
    def lesFraFil(self, filnavn):
        """
        Metoden som tar en fil med 2 verdier separert med semikolon som parameter.
        Legger verdiene inn i listen av sanger .
        
        """
        # Renser spillelisten i tilfelle man legger inn listen flere ganger              
        self._sanger.clear()

        # Les en fil med musikk
        #innfil = open(filnavn, mode='r')
        with open(filnavn, mode="r") as innfil:
                 
            for i, linje in enumerate(innfil):
                biter = linje.strip().split(';')
                sang = Sang(biter[0], biter[1])
                
                # Legg objektet(sangen) til i spillelisten
                self._sanger.append(sang)
                      
        # Lukk filen
        #innfil.close() # with with lukkes filen automagisk.
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
        print(f"Nå spilles denne: {sang}")
        
    def finnSang(self, tittel):
        """ Metoden finner en sang i spillelisten ved å søke etter tittel """
        for sang in self._sanger:
            if sang._tittel == tittel:
                return sang
            
    def hentArtistUtvalg(self, artistnavn):
        """ 
        Metoden leter etter sanger med samme artist. Artist spesifiseres som parameter
        Returnerer en liste med sangene av artisten.
        """
        sangliste = []
        for sang in self._sanger:
            # Hvis artisten finnes så legges sanen til listen
            if artistnavn in sang._artistList:
                sangliste.append(sang)

        return sangliste

        
    def fjernSang(self, sang):
        """ Metoden fjerner en sang fra spillelisten """
        self._sanger.remove(sang)
        
# main function to run the file individually        
def main():
    music = Spilleliste('Hele musikkbiblioteket')
    music.lesFraFil("musikk.txt")
    print(music)



if __name__ == "__main__":
    
    main()
    
