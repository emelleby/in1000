#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 00:58:14 2020

@author: eivind
"""

def leggTil() :
    sangliste = []
    artist = input('Oppgi navn på band/artist: ')
    tittel = input('Oppgi navn på sang: ')
    while artist != "" :
        #nySang = Person(artist, tittel)
        sangliste.append((tittel,artist))
        artist = input('Oppgi navn på band/artist: ')
        tittel = input('Oppgi navn på sang: ')
        
    # Skriv sanger til musikk.txt
    skrivsang = open("musikk.txt", "a")
    
    for sang in sangliste:
        linje = sang[0] + ";" + sang[1] + '\n'
        skrivsang.write(linje)
        
    skrivsang.close()
    

    
if __name__ == "__main__":
    #def main():
    
    leggTil()