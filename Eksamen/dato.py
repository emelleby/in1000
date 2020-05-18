#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:46:36 2020

@author: eivind
"""

class Dato:
    def __init__(self, maaned, dag, aar, d):
        
        self._aar = aar
        self._maaned = maaned
        self._dag = dag
        self._str = d
        
        self._sort = 0
        
        m = "0" + str(maaned) if maaned<10 else maaned
        d = "0" + str(dag) if dag<10 else dag
        sort = str(aar)+ str(m)+str(d)
        self._sort = int(sort)
        # print("Jeg er initiert")
    
    # Sørger for at jeg kan bruke objektet som nøkkel i dict 
    def __hash__(self):
        return hash((self._dag, self._maaned, self._aar))
    """    
    def __eq__(self, annen):
        return (self._aar == annen._aar and 
        self._maaned == annen._maaned and
        self._dag == annen._dag)
    """    
    def __del__(self):
        print("Jeg har blitt erstattet")
        

    def __eq__(self, annen):
        return (self._dag, self._maaned, self._aar) == (annen._dag, annen._maaned, annen._aar)

    def __ne__(self, annen):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == annen)
        
    def __str__(self):
        return f"Min dato er: {self._dag}.{self._maaned}.{self._aar}"
    
    def getDato(self):
        return (self._dag, self._maaned, self._aar)
    
    def getSort(self):
        return self._sort
    
    def string(self):
        return f'"{self._str[0]}{self._str[1]}, {self._str[2]}"'
        