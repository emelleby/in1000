#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:09:47 2020

@author: eivind
"""
from land import Land
from smitte import Smitte


class Region(Land):
       
    def __init__(self, navn, kode, land):
        
        self._navn = navn
        self._kode = kode
        self._land = land
        self._smitte = {}
        self._smitteArr = None
        self._smitteSortedByAnt = None

        
        for l in self._land:
            # for hvert smitteobjekt hvert land har
            smitte = l.getSmitte()

            for ele in smitte:
                # print(ele)
                d = ele.getDato()
                # Hvis dato er i ordbok
                if d in self._smitte:
                    # hent elementets smittetall
                    smitte = ele.getSmitteDato()
                    # Legg til elementets smittetall til i det objektet som er der
                    self._smitte.get(d).updateSmitte(smitte)
                    
                else:
                    self._smitte[d] = Smitte(ele.getSmitteDato())

        # Sorter self._smitte
        self._smitteArr = sorted(self._smitte.items(), key=lambda x: x[0].getSort()) #reverse=True
        self._smitteSortedByAnt = sorted(self._smitte.items(), key=lambda x: x[1].getSmitteDato())
        
        # Use List comprehension to print the contents of dictionary , sorted by value of an object attribute in the key.
        #[ print(key , " :: " , value) for (key, value) in sorted(self._smitte.items(),  key=lambda x: x[0].getSort() ) ]
    
    
    def __str__(self):
        navnLand = []
        for land in self._land:
            navnLand.append(land.getNavn())
        navn = ", ".join(navnLand)
        return f"Jeg er en region som heter {self._navn} med følgende land: {navn}"
    
    def getNavnRegion(self):
        return self._navn
        
    def setKode(self, kode):
        self._kode = kode
        
    def printSmitteSortedDate(self):
        for key,value in self._smitteArr:
            print(key,value)
            
    def printSmitteSortedAnt(self):
        for key,value in self._smitteSortedByAnt:
            print(key,value)
            
    def getSmitteSortedDate(self):
        return self._smitteArr

            
    def getSmitteSortedAnt(self):
        return self._smitteSortedByAnt

        




# Comment