#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:56:09 2020

@author: eivind
"""

from dato import Dato

def erstatt(argument):
    bok = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }
    return bok.get(argument, "Ugyldig måned")

def dato(dato):
    datoer = {}
    
    # Opprett et datoobjekt    
    #Apr82020 = Dato(4, 8, 2020)
    # Legg datoobjektet inn i ordboken 'datoer
    #datoer["Apr82020"] = Apr82020
    #print objektet
    #print(Apr82020)
    # print ordboken
    #print(datoer)
    # Spør om den dato på formen Mmmdåååå
    #dato = input("dato: ")
    # Hvis strengen som ble gitt er i ordboken som key
    if dato in datoer:
        # Pek datoen som ble gitt til det objektet
        dato = datoer[dato]
        print(dato)
        print("46")
        
    else:
        # Legg datoobjektet inn i listen
        datoer[dato] = Dato(erstatt(dato[:3]), int(dato[3]), int(dato[4:]))
        # Pek landobjektets datoattributt til objektet
        
        
    print(datoer)
    #print(datoer[dato])

    
    # assert(apr82020 is dato)

def main():
        
    print(erstatt("Apr"))
    print(type(erstatt("Apr")))

if __name__ == "__main__":
    main()