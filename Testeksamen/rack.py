#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 09:59:43 2020

@author: eivind
"""

from node import Node

class Rack:
    """
    Klassen Rack skal lagre Node-objektene som hører til et rack i en liste. 
    Vi skal kunne legge til noder i racket hvis det er færre enn maks antall noder der fra før.
    """
    def __init__(self, limit):
        self._limit = limit
        self._noder = []
        
    def __str__(self):
        return f"{len(self._noder)} noder i dette racket"
        
    def leggTilNode(self, ram, cpu):
        self._noder.append(Node(ram, cpu))
    
    def antallNoder(self):
        # returner antall noder i racket
        return len(self._noder)
    
    def fulltRack(self):
        if len(self._noder) < self._limit:
            return False
        return True
    
    def getNoder(self):
        
        return self._noder