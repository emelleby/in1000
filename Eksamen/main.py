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
from functions import erstatt, country, new, date, remove, group, maks, write#, test

# Ordbok som holder på kode og navn for hvert land
landkoder = {}

# Her lagres all data
smittedata = {}

datoer = {}

# Her lagres regioner som blir opprettet av bruker 
regioner = {}

def main():
    innfil = "data.csv"
    #innfil = input("Hva heter filen med smittedata? ")
   
    #Åpne filen og les linje for linje
    with open(innfil, mode='r') as data:
        # dataListe for å holde data gjennom hele mainfunksjonen
        dataListe = []
        
        # Opprett et set med unike verdier av landkoder med tilhørende navn
        landSet = set()
        for linje in data:
            biter = linje.strip().split(",")
            s = (biter[1],biter[0])
            landSet.add(s)
            
            # Legg data fra fil inn i dataListe
            dataListe.append(biter)

        # print(dataListe)
        for landkode in landSet:
            landkoder[landkode[0]] = landkode[1]
             
        # Iterer over dataSet
        for e in dataListe:

            # Initier variabler for objektene
            if e[1] in smittedata:
                land = smittedata.get(e[1])
                    
            # Hvis vi ikke har sett landkoden før så oppretter vi et nytt objekt av klassen Land
            if e[1] not in smittedata:
                land = Land(e[0], e[1])

            # Opprett et Smitte objekt 
            smitte = Smitte(int(e[4]))
            
            # Splitt og konfig en tuple med tre dato elementer(m,d,å)
            d = (e[2][1:4], e[2][4:], e[3][-5:-1])

            # Lag datostrengen som skal være key i datoer{}
            datoen = (e[2][1:]) + (e[3][-5:-1])
            
            # Hvis strengen som ble gitt er i ordboken som key - Dato er opprettet
            if datoen not in datoer:
                
                # Legg datoobjektet inn i listen over datoer
                datoer[datoen] = Dato(erstatt(datoen[:3]), int(d[1]), int(d[2]), d)

            # Sett dato på smitteobjektet
            smitte.setDato(datoer[datoen])
            
            # Sett smittedata for denne dato for landet
            land.setSmitte(smitte)
            
            # Legg Til land i smittedata med kode som key
            smittedata[e[1]] = land
                
        print("Data lastet inn\n")

    print("Her begynner løkken for meny.")

    menyValg = {
                "c": country,
                "d": date,
                "g": group,
                "m": maks,
                "n": new,
               # "p": plot,
               # "q": avslutt,
                "r": remove,
                #"t": test,
                "w": write            
                }
    
    valg = ""

    while valg != "q":
        

        valg = input(f"Hva vil du gjøre? ")
        
        if valg == "m":
            menyValg.get(valg)(regioner)
            continue
        
        if valg == "g":

            r = menyValg.get(valg)(smittedata, datoer)
            # Opprett Region
            region = Region(r[0], r[1], r[2])
            # Legg region som er opprettet til i ordboken {'Navn': 'Region'}
            regioner[r[0]] = region
            print(regioner)
            continue
        
        # Plukk funksjoner fra menyen eller avslutt
        if valg != "q":
            menyValg.get(valg)(smittedata, datoer)
            

            
    print("Takk for nå.")    
        
if __name__ == "__main__":
    main()
