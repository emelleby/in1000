#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:56:09 2020

@author: eivind
"""

# from dato import Dato

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
        print(landSmitte)
        print(landSmitte[0])
        for day in landSmitte[1]:
            print(day.getSmitte())
            
def date(sdata, datoer):
    obj = None
    d = 8 #int(input("Dag"))
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
    # print(sdata)    
    print(sdata.get("NOR").getSmitteDay(obj)) 
    
    smitte = 0    
    for k, land in sdata.items():
        print(k)
        arr = land.getSmitteArr()
        print(arr)
        for i in arr[1]:
            if i.getDato() == obj:
                print("Hei")
                smitte += i.getSmitteDato()
    
    print(smitte)

def new(x,y):
    print("Jasså, så du vil ha noe nytt? Sorry!")



def main():
        
    print(erstatt("Apr"))
    print(type(erstatt("Apr")))

if __name__ == "__main__":
    main()