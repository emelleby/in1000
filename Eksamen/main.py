#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:49:27 2020

@author: eivind
"""
from land import Land
from smitte import Smitte
from dato import Dato
from region import Region
from erstatt import erstatt#, dato

def main():
    innfil = "data.txt"
    # innfil = input("Hva heter filen med smittedata? ")
    
    # Ordbok som holder på kode og navn for hvert land
    landkoder = {}
    
    smittedata = {}
    
    datoer = {}
    
    #Åpne filen og les linje for linje
    with open(innfil, mode='r') as data:
        
        dataListe = []
        
        landSet = set()
        for linje in data:
            biter = linje.strip().split(",")
            s = (biter[1],biter[0])
            landSet.add(s)
            
            dataListe.append(biter)

        print(landSet)
        for landkode in landSet:
            landkoder[landkode[0]] = landkode[1]
            # Opprett en Objekt av klassen 'Land'
            
        print(landkoder)
        
        lkode = ""
        # print(dataListe)
        
        # Iterer over dataSet
        for e in dataListe:

            # Initier variabler for objektene
            if e[0] in smittedata:
                land = smittedata.get(e[0])

            else:

                land = None

            dato = None

            
            # Hvis vi ikke har sett landkoden før så oppretter vi et nytt objekt av klassen Land
            if lkode != e[1]:
                land = Land(e[0], e[1])

                lkode = e[1]

            # Opprett et Smitte objekt 
            smitte = Smitte(e[4])
              
            # Lag datostrengen
            datoen = (e[2][1:]) + (e[3][-5:-1])
            
            # Hvis strengen som ble gitt er i ordboken som key
            if datoen in datoer:
                
                # Pek dato til verdien i datoer
                dato = datoer[datoen]
                
                # Pek datoObjektet til smitte objektet
                smitte.setDato(dato)
                
                land.setSmitte(smitte)
                
                # Legg Til land i smittedata
                smittedata[e[0]] = land
            
            # Hvis landet ikke er i smittedata
            else:
                # Legg datoobjektet inn i listen over datoer
                datoer[datoen] = Dato(erstatt(datoen[:3]), int(datoen[3]), int(datoen[4:]))
                dato = datoer[datoen]
                smitte.setDato(dato)
                
                land.setSmitte(smitte)
                
                # Legg Til land i smittedata
                smittedata[e[0]] = land
                
                #print("objekt sent til smittedata")
        print(smittedata["Norway"])
        print(smittedata["Sweden"])
        print(smittedata)
        #print(erstatt((biter[2][1:4])))
        #print((biter[2][1:4]))
    print("Hei")
    #print(datoer)
    c = "Norway"
    if c in smittedata:
        land = smittedata.get(c)
        print(land)
        landSmitte = land.getSmitteArr()
        print(landSmitte)
        print(landSmitte[0])
        for day in landSmitte[1]:
            print(day.getSmitte())
                     
                
    #print(data)
    
    
    
if __name__ == "__main__":
    main()
