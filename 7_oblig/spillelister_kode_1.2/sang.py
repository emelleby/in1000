#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:13:54 2020

@author: eivind
"""

class Sang:
    """
    class Sang tar en artist og en tittel som parametre og leverer metodene 'spill',
    'sjekkArtist', 'sjekkTittel' og 'SjekkArtistogTittel'
    
    """
    def __init__(self, tittel, artist):
        """ 
        Initierer en instans av sang med artist og tittel på sangen
        Splitter opp sangtittel og artistnavn i egne lister for å hjelpe søk.
        """
        self._artist = artist
        self._tittel = tittel
        # Splitter parameter opp i lister for å bruke i metoder
        self._artistList = artist.split()
        self._tittelList = tittel.split()
        
    def __str__(self):
        return f"Artisten er: {self._artist}. Tittel: {self._tittel}"
        
        
    def spill(self):
        """
        Metoden printer en string med hva som spilles.
        """
        # print(f"Spiller av {self._tittel} med {self._artist}") # or
        # print(f"Spiller følgende: {str(self)}") # or
        print("Spiller følgende:", self)
    
    def sjekkArtist(self, navn):
        """
        Metoden returnerer True dersom ett eller flere av navnene i strengen navn finnes i _artist, ellers False.
        """
        sjekk = navn.split()
        artistList = [v.lower() for v in self._artistList]
        
        # sjekk om søkestrengen inneholder ord som matcher artist
        for ord in sjekk:
            if ord.lower() in artistList:
                return True
        return False
    
    def sjekkTittel(self, tittel):
        """
        Metoden sjekker om oppgitt tittel er den samme som i instansvariabelen og returnerer True ved likhet, ellers False
        """
        sjekk = tittel.split()
        tittelList = [v.lower() for v in self._tittelList]
        
        for ord in sjekk:
            if ord.lower() in tittelList:
                return True
        return False
    
    def sjekkArtistogTittel(self, artist, tittel):
        """
        Metoden returnerer True dersom både tittelen og artisten
        stemmer med sangens instansvariabler, ellers False.
        """
        return True if self.sjekkArtist(artist) and self.sjekkTittel(tittel) else False

       
        
        