#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:56:09 2020

@author: eivind
"""

from region import Region

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
    c = input("Oppgi kode for landet du vil se: ")
    if c in smittedata:
        land = smittedata.get(c)
        # print(land)
        landSmitte = land.getSmitteArr()
        # print(landSmitte)
        print(landSmitte[0])
        for day in landSmitte[1]:
            print(day.getSmitte())
            
def date(sdata, datoer):
    obj = None
    d = 19 #int(input("Dag"))
    m = 4 #int(input("Måned"))
    aa = 2020 #int(input("År"))
    t = (d,m,aa)
    print(t)
    # Finn det riktige dato objektet
    for key, dato in datoer.items():
        
        if dato.getDato() == t:
            obj = dato
            print("Fant dato")
            print(obj)
            break
    # print(sdata)    
    # print(sdata.get("NOR").getSmitteDay(obj)) 
    
    smitte = 0    
    for k, land in sdata.items():
        print(k)
        arr = land.getSmitteArr()
        print(arr)
        for i in arr[1]:
            if i.getDato() == obj:
                
                smitte += i.getSmitteDato()
                break
    print(smitte)
   
def remove(data, dato):
    for k, land in data.items():
        print(k)
        arr = land.getSmitteArr()
        print(arr)
        for i,o in enumerate(arr[1]):
            if o.getSmitteDato() == 0:
                land.deleteSmitte(i)


def new(x,y):
    print("Jasså, så du vil ha noe nytt? Sorry!")

def group(data,dato):
    navn = "NS" #input("Hva skal gruppen hete? " )
    kode = "NSkode"#input("Hvilken kode vil du ha på gruppen? ")
    l = "NOR,DEN" #input("Skriv landkoder. Separert med komma.")
    l2 = l.split(",")
    print(l2)
    
    land = []
    for v in l2:
        if v in data:
            land.append(data[v])
    
    # Opprett et Regionsobjekt
    region = Region(navn, kode, land)
    #region.setNavn(navn)
    #region.setKode(kode)
    # print(region.getSmitteArr())        
    print(region)
    return region
    #regionSmitte = region.getSmitteArr()
        # print(landSmitte)
    #print(regionSmitte[0])
    #for day in regionSmitte[1]:
        #print(day.getSmitte())
    

def main():
    pass
    

if __name__ == "__main__":
    group(data=1,dato="w")