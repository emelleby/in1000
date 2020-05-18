#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:09:47 2020

@author: eivind
"""
from land import Land
from smitte import Smitte
# from dato import Dato


class Region(Land):
    
    # Bruk av super()    
    def __init__(self, navn, kode, land):
        
        self._navn = navn
        self._kode = kode
        self._land = land
        self._smitte = {}
        self._smitteArr = None
        self._smitteSortedByAnt = None
        # super().__init__(self) # Tar inn '_navn' og '_kode' fra 'Land' konstruktør
        
        for l in self._land:
            # for hver smitteobjekt hvert land har
            smitte = l.getSmitteArr()
            # d=None
            for ele in smitte[1]:
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
        
        
        #print(self._smitteArr)
        #print(self._smitteSortedByAnt)
        
    def __str__(self):
        return f"Jeg er en region som heter {self._navn} med følgende land: {i.getNavn() for i in self._land}\n {self.printSmitteSortedAnt()}"
    
    def getNavn(self):
        return self._navn
        
    def setKode(self, kode):
        self._kode = kode
        
    def printSmitteSortedDate(self):
        for key,value in self._smitteArr:
            print(key,value)
            
    def printSmitteSortedAnt(self):
        for key,value in self._smitteSortedByAnt:
            print(key,value)
            
        # Use List comprehension to print the contents of dictionary , sorted by value of an object attribute in the key.
        #[ print(key , " :: " , value) for (key, value) in sorted(self._smitte.items(),  key=lambda x: x[0]._sort ) ]




# Comment