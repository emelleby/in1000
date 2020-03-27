#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:44:22 2020

@author: eivind
"""

# fra filnavn uten filext importeres Klassenavn(modul) som kallenavn(M)
from motorsykkel import Motorsykkel as M

def hovedprogram():
    # Lag en instance a klassen og kall den "honda"
    honda = M("Honda", "PO1234", 1234)
    tri = M("Triuph", "BS3211", 34678)
    hd = M("Harley Davidson", "hd9876", 43211)
    
    # test at __str__ metoden virker
    print(hd)
    
    # test at kjor() virker
    #M.kjor(hd, 10) # ikke slik, men slik..
    hd.kjor(10)
    
    # verifiser kjor()
    print(f"Nå har den kjørt et par kilometer og da er det {hd.hentKilometerstand()}")
    
    # test hentKilometerstand()
    print(M.hentKilometerstand(hd))
    print(hd.hentKilometerstand())
    
    # test skrivUt (Dinne er visst feil)
    #print(M.skrivUt(honda))

    print(honda.skrivUt())
    print(tri.skrivUt())
    print(hd.skrivUt())
    
    # Skriver ut hjelp for Class Motorsykkel(M)
    # qhelp(M)
    
hovedprogram()