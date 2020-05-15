#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 16:56:29 2020

@author: eivind
"""

landkoder = {}

smittedata = {}

datoer = {}

dataListe = [['Sweden', 'SWE', '"Apr8', ' 2020"', '12345', '31'], ['Norway', 'NOR', '"Apr9', ' 2020"', '6010', '33'], ['Sweden', 'SWE', '"Apr19', ' 2020"', '15234', '42'], ['Denmark', 'DEN', '"Apr8', ' 2020"', '1988', '30'], ['Norway', 'NOR', '"Mar7', ' 2020"', '1', '-1'], ['Norway', 'NOR', '"Apr7', ' 2020"', '5755', '31'], ['Norway', 'NOR', '"Apr8', ' 2020"', '5863', '32']]
                
landSet = set()
for l in dataListe:

    s = (l[1],l[0])
    landSet.add(s)

for landkode in landSet:
    landkoder[landkode[0]] = landkode[1]


lkode = ""

# Iterer over dataSet
for e in dataListe:

    # Initier variabler for objektene
    if e[1] in smittedata:
        land = smittedata.get(e[1])

    else:

        land = None
            
    # Hvis vi ikke har sett landkoden før så oppretter vi et nytt objekt av klassen Land
    if lkode != e[1]:
        land = Land(e[0], e[1])

        lkode = e[1]

    # Opprett et Smitte objekt 
    smitte = Smitte(int(e[4]))
    
    # Splitt og konfig en tuple med tre dato elementer(m,d,å)
    d = (e[2][1:4], e[2][4:], e[3][-5:-1])
    print(d)
    # Lag datostrengen som skal være key i datoer{}
    datoen = (e[2][1:]) + (e[3][-5:-1])
    
    # Hvis strengen som ble gitt er i ordboken som key - Dato er opprettet
    if datoen not in datoer:
        
        # Legg datoobjektet inn i listen over datoer
        datoer[datoen] = Dato(erstatt(datoen[:3]), int(d[1]), int(d[2]))
        
    
    # Sett dato på smitteobjektet
    smitte.setDato(datoer[datoen])
    
    # Sett smittedata for denne dato for landet
    land.setSmitte(smitte)
    
    # Legg Til land i smittedata med kode som key
    smittedata[e[1]] = land
        
print(smittedata["NOR"])
print(smittedata["SWE"])
print(smittedata)