#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:28:24 2020

@author: eivind
"""

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
        return f"Landet er {self._navn}({self._kode}) og har smittede: {self._smitte})"
    
    def setSmitte(self, smitte):
        
        self._smitte.append(smitte)
        # print("Running setSmitte")
        
    def getSmitteArr(self):
        days = []
        for day in self._smitte:
            
            days.append(day)
        return (self._navn, days)
        