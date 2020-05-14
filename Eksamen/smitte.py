#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:38:12 2020

@author: eivind
"""

class Smitte:
    """
    Klassen Smitte inneholder informasjon om smittestatus på en bestemt dato for et land. 
    Smittestatus er antall som har testet positivt for covid-19 i dette landet på den gitte dato. 
    Klassen skal ha instansvariable for antall smittede, antall testet, antall innlagt på sykehus, 
    antall på respirator og antall døde av covid-19 for landet for den datoen som instansvariabelen 
    dato refererer til. Det skal ikke være noen instansvariabel for land i Smitte. 
    Informasjonen om hvilket land smitteregistreringen gjelder, ligger i landobjektet 
    som inneholder smitteregistreringen.
    """
    def __init__(self, antSmittede):
        
        self._antSmittede = antSmittede
        self._antTestet = None
        self._antSykehus = None
        self._antRespirator = None
        self._antDoede = None
        self._dato = None
        
        
    def __str__(self):
        return f"Antallsmittede er {self._antSmittede}"
    
    def setDato(self, dato):
        self._dato = dato
        
    def getSmitte(self):
        return (str(self._dato), self._antSmittede)