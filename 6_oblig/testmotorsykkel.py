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
    M.kjor(hd, 10)
    
    # verifiser kjor()
    print(f"Nå har den kjørt et par kilometer og da er det {M.hentKilometerstand(honda)}")
    
    # test hentKilometerstand()
    print(M.hentKilometerstand(honda))
    
    # test skrivUt
    print(M.skrivUt(honda))
    print(M.skrivUt(tri))
    print(M.skrivUt(hd))
    
    # Skriver ut hjelp for Class Motorsykkel(M)
    help(M)
    
hovedprogram()