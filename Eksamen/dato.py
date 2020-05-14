#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:46:36 2020

@author: eivind
"""

class Dato:
    def __init__(self, maaned, dag, aar):
        
        self._aar = aar
        self._maaned = maaned
        self._dag = dag
        
        # print("Jeg er initiert")
    
    # Sørger for at jeg kan bruke objektet som nøkkel i dict 
    def __hash__(self):
        return hash((self._dag, self._maaned, self._aar))
        
    def __eq__(self, annen):
        return (self._aar == annen._aar and 
        self._maaned == annen._maaned and
        self._dag == annen._dag)
        
    def __del__(self):
        print("Jeg har blitt erstattet")
        

    #def __eq__(self, annen):
        #return (self._dag, self._maaned, self._aar) == (annen._dag, annen.maaned, annen._aar)

    def __ne__(self, annen):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == annen)
        
    def __str__(self):
        return f"Min dato er: {self._dag}.{self._maaned}.{self._aar}"