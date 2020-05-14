#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 09:54:44 2020

@author: eivind
"""

class Node:
    """
    Klassen Node representerer en datakraft node i et rack
    """
    
    def __init__(self, ram, cpu):
        
        self._ram = ram
        self._cpu = cpu
        
    def __str__(self):
        
        return f"Noden har {self._ram} GB RAM og {self._cpu} CPU(er)."
    
    def getNode(self):
        # Returns a tuple with info
        return (self._ram, self._cpu)