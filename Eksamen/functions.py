#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:56:09 2020

@author: eivind
"""


def erstatt(argument):
    bok = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }
    return bok.get(argument, "Ugyldig måned")

def country(smittedata, datoer):
    """Country"""
    c = input("Oppgi kode for landet du vil se: ")
    if c in smittedata:
        land = smittedata.get(c)

        landSmitte = land.getSmitteArr()

        print(landSmitte[0])
        for day in landSmitte[1]:
            print(day.getSmitte())
 
           
def date(sdata, datoer):
    """Skriver ut data om smitte for en bestemt dato"""
    obj = None
    d = int(input("Dag: "))
    m = int(input("Måned: "))
    aa = int(input("År: "))
    t = (d,m,aa)

    # Finn det riktige dato objektet
    for key, dato in datoer.items():
        
        # Hvis en dato er lik det bruker har oppgitt
        if dato.getDatoTuple() == t:
            obj = dato
            # break kunne vært her for å avslutte loopen for performance
            
    # For å beregne totalt antall smittede
    smitte = 0
    
    for k, land in sdata.items():

        arr = land.getSmitteArr()

        for i in arr[1]:
            if i.getDato() == obj:
                print(arr[0],obj, i.getSmitteDato())
                smitte += i.getSmitteDato()
                # break
    print("Totalt antall smittede er : " +str(smitte))

   
def remove(data, dato):
    """Sletter alle oppføringer i datagrunnlaget hvor smitteantallet = 0"""
    ant = 0
    for k, land in data.items():
        # Hent all smittedata
        arr = land.getSmitte()
        
        # Hvis smitten er lik null slettes oppføringen
        # Det forutsettes at ikke smitte går tilbake til null når det først er blitt tilfeller.
        for i, obj in enumerate(arr):
            if obj.getSmitteDato() == 0:
                land.deleteSmitte(i)
                ant += 1
                
    print(str(ant) + " oppføringer ble fjernet")
    
    
def new(x,y):
    print("Jasså, så du vil ha noe nytt? Sorry!")

def group(data, dato):
    """Oppretter en region med en gruppe land"""
    navn = input("Hva skal gruppen hete? " )
    kode = input("Hvilken kode vil du ha på gruppen? ")
    l = input("Skriv landkoder. Separert med komma.")
    l2 = l.split(",")

    # Legg til landskoder hvis de ikke er der fra før
    land = []
    for i in l2:
        if i in data.keys():
            land.append(data.get(i))
    
    return (navn,kode,land)
    

def maks(regioner):
    """Hvis en region er opprettet så kan man få svar på hvilken dato smitten økte mest"""
    print("Hvilken region vil du vite maks av?")

    for region in regioner.keys():
        print(region)
        
    regionvalg = input("Skriv inn valget: " )
    regionSmitte = regioner[regionvalg].getSmitteSortedAnt()

    # Datoobjektet.
    d = None
    smitteokning = 0
    dayBefore = 0
    for dato, smitte in regionSmitte:
        day = smitte.getSmitteDato()
        dayOkning = day - dayBefore
        dayBefore = day
        if dayOkning > smitteokning:
            smitteokning = dayOkning
            d = dato
            
    print(str(d) + " med " + str(smitteokning) + " nye smittede.")
    
def write(data, datoer):
    """Skriver data ut igjen slik at utskrift kan brukes som input. Filen vil hete 'out.csv'"""

    skriv = open("out.csv", mode="w")

    # sort data
    dataSorted = sorted(data.items())

    for land in dataSorted:
        skriv.write(land[1].string())

        
    skriv.close()
    print("Oppføringer skrevet til filen 'out.csv'")

def main():
    pass
    

if __name__ == "__main__":
    main()