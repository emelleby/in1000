#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:09:47 2020

@author: eivind
"""
from land import Land


class Region(Land):
    """
    def __init__(self, navn, kode):
        
        self._navn = navn
        self._kode = kode
    
    # Bruk av super()    
    def __init__(self, land):
        
        self._land = land
        super().__init__(self) # Tar inn '_navn' og '_kode' fra 'Land' konstruktør
    """
    _land = [] # Landkode eller Id?