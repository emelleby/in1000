#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:40:05 2020

@author: eivind
"""

class Hund:
    def __init__(self, alder, vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 3

    def __str__(self):
        return f"Hunden er {self._alder} aar, veier {self._vekt} kilo og er {self._metthet * 10}% mett."

    def hentAlder(self):
        """ returnerer alder """
        return self._alder

    def hentVekt(self):
        """ Returnerer vekt """
        return self._vekt
    
    def spis(self, mat):
        """ Spisefunksjon som legger input til metthet og oker vekten med en kilo om hunden er over 70% mett """
        self._metthet += mat
        self._vekt += 1 if self._metthet > 7 else 0
        #if self._metthet > 7:
            #self._vekt += 1

    def spring(self):
        self._metthet -= 1
        self._vekt -= 1 if self._metthet < 5 else 0
        #if self._metthet < 5:
            #self._vekt -= 1

