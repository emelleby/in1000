#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:28:24 2020

@author: eivind
"""

from operator import itemgetter, attrgetter

class Land:
    
    def __init__(self, navn, kode):
        
        self._navn = navn
        self._kode = kode
        # self._dato = First date?
        self._smitte = [] # Data må lagres her i en Liste med dict
        
    # Sørger for at jeg kan bruke objektet som nøkkel i dict 
    def __hash__(self):
        return hash((self._navn, self._kode))
        
    def __eq__(self, annen):
        return (self._navn == annen._navn and 
        self._kode == annen._kode)

        
    def __str__(self):
        return f"Landet er {self._navn}({self._kode}) og har smittede: {self._smitte}"
        
    
    def setSmitte(self, smitte):
        self._smitte.append(smitte)

    # I tilfelle man vil slette smittedata    
    def deleteSmitte(self, index):
        del self._smitte[index]
    
    def getSmitte(self):
        return self._smitte
    
    # Leverer smittedata sammen med navn på landet
    def getSmitteArr(self):
        days = []
        for day in self._smitte:
            
            days.append(day)
        return (self._navn, days)
    """
    def getSmitteDay(self, dato):
        for day in self._smitte:
            print(day.getDato())
            if day.getDato() == dato:
                smitte = day.getSmitte()[1]
                print("HEI")
                return smitte #day.getSmitteDato()
            else:
                return 0
     """       
    def getNavn(self):
        return self._navn
    
    # Leverer stringen som skal skrives til fil
    def string(self):
        stringArr = []
        # Sorterer på dato slik at det blir alfabetisk og på dato ut(kan skrives om litt)
        self._smitte.sort(key=lambda x: x.getDato().getSort())
        string = ""
        for dato in self._smitte:
            stringArr.append(self._navn + "," + self._kode + "," + dato.string() + '\n')
        
        return string.join(stringArr)
            
        