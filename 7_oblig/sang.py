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
    def __init__(self, artist, tittel):
        self._artist = artist
        self._tittel = tittel
        
    def __str__(self):
        return f"Artisten er: {self._artist}. Tittel: {self._tittel}"
        
        
    def spill(self):
        """
        Metoden returnerer en string med hva som spilles.
        """
        return f"Spiller av {self._tittel} med {self._artist}"
    
    def sjekkArtist(self, navn):
        """
        Metoden returnerer True dersom ett eller flere av navnene i strengen navn finnes i _artist, ellers False.
        """
        True if navn.lower() == self._artist.lower() else False
        
        
        