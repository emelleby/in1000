#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:13:54 2020

@author: UIO & eivind
"""

from sang import Sang
from spilleliste import Spilleliste
from leggtil import leggTil as leggtil

def hovedprogram():
    
    filnavn = "musikk.txt"
    # Opprett en spilleliste for filen med navnet på filen minus fil.ext
    for i, char in enumerate(filnavn):
        if char == ".":
            navn = filnavn[:i].capitalize()
            allMusikk = Spilleliste(navn)
            # print(navn) # musikk
    
    # allMusikk = Spilleliste('Hele musikkbiblioteket')
    allMusikk.lesFraFil(filnavn)
    
    print("Tester spillAlle(): Spiller alle sanger i listen:")
    allMusikk.spillAlle()
    print()
    
    leggtil()
    
    allMusikk.lesFraFil(filnavn)
    
    nySang = Sang("Mil etter mil", "Jahn Teigen")
    allMusikk.leggTilSang(nySang)
    print("Spiller alle sanger i listen inkl ny sang:")
    allMusikk.spillAlle()
    print()
    
    print("Spiller ny sang:")
    allMusikk.spillSang(nySang)
    print()
    
    funnetSang = allMusikk.finnSang("Mil etter mil")
    if funnetSang is not None:
        print("Fant sangen:")
        allMusikk.spillSang(funnetSang)
    else:
        print("Fant ikke sangen\n")
    assert(funnetSang in allMusikk.hentArtistUtvalg("Jahn"))
    print()
    
    # Tester om flere sanger returneres for samme artist
    queenListe = allMusikk.hentArtistUtvalg("Queen")
    print("Spiller sanger med Queen hentet fra listen: ")

    for queenSang in queenListe:
        allMusikk.spillSang(queenSang) 
        #queenSang.spill()
    
    # Tester om funnetSang er fjernet fra listen
    allMusikk.fjernSang(funnetSang)
    assert(not (funnetSang in allMusikk.hentArtistUtvalg("Jahn")))
    print()
    
    #Tester Spilleliste() ___str__ metode
    print(allMusikk)
    
hovedprogram()
