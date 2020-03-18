#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:40:05 2020

@author: eivind
"""

class Hund:
    def __init__(self, alder, vekt):
        self.alder = alder
        self.vekt = vekt
        self.metthet = 3

    def __str__(self):
        return f"Hunden er {self.alder} aar, veier {self.vekt} kilo og er {self.metthet * 10}% mett."

    def spis(self, mat):
        """ Spisefunksjon som legger input til metthet og oker vekten med en kilo om hunden er over 70% mett """
        self.metthet += mat
        self.vekt += 1 if self.metthet > 7 else 0
        #if self.metthet > 7:
            #self.vekt += 1

    def spring(self):
        self.metthet -= 1
        self.vekt -= 1 if self.metthet < 5 else 0
        #if self.metthet < 5:
            #self.vekt -= 1

