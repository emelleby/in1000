#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 00:58:14 2020

@author: eivind
"""

def leggTil() :
	personliste = []
	les = input('Oppgi navn: ')
	while les != "" :
		navnene = les.split()
		nytt = Navn(navnene[0],navnene[1],navnene[2])
		alder = int(input("Oppgi alder: "))
		nyPerson = Person(nytt, alder)
		personliste.append(nyPerson)
		les = input("Oppgi navn på naturlig form: ")