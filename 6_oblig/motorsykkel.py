#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:38:48 2020

@author: eivind

Oppgave 2: Motorsykkel
###Filnavn: motorsykkel.py og testMotorsykkel.py

1. Skriv klassen Motorsykkel med en konstruktør (init-metode) som initierer de
instansvariablene klassen trenger.
"""

class Motorsykkel:
    """
    Representerer en motorsykkel som har et merke, et registreringsnummer og kilometerstand.
    """
    def __init__(self, merke, registreringsnummer, kilometerstand):
        self.merke = merke
        self.registreringsnummer = registreringsnummer
        self.kilometerstand = kilometerstand

    def __str__(self):
        """ returnerer en string om tilstanden til instansen """
        return f"Sykkelen er en {self.merke}, med registreringsnummer \
{self.registreringsnummer} og har kilometerstand: {self.kilometerstand}."

    def kjor(self, km):
        """ Legger til kilometer som kjøres til kilometerstand """
        self.kilometerstand += km

    def hentKilometerstand(self):
        """ returnerer kilometerstanden som int """
        return self.kilometerstand

    def skrivUt(self):
        """ PRINTER en string om tilstanden til instansen """
        print(f"Sykkelen er en {self.merke}, med registreringsnummer \
{self.registreringsnummer} og har kilometerstand: {self.kilometerstand}.")
