#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:00:03 2020

@author: eivind
"""
from regneklynge2 import Regneklynge
# from rack import Rack

def main():
    #Opprett en regneklynge
    abel = Regneklynge("klynge.txt", "abel")
    
    
    
    print(abel)
    print(abel.getRack(-1))
    
    # prin = abel.getRack(-1)
    print(666%12)
    
    # print(Rack.getNoder(prin))
    
    print("Regneklyngen har følgende antall prosessorer: " + str(Regneklynge.antProsessorer(abel)))
    
    print("Antall noder med 128GB eller mer er: " + str(Regneklynge.noderMedNokMinne(abel, 128)))
    
    print()
    print("Her kommer utskriften:")
    print("Antall noder med 32GB eller mer er: " + str(Regneklynge.noderMedNokMinne(abel, 32)))
    print("Antall noder med 64GB eller mer er: " + str(Regneklynge.noderMedNokMinne(abel, 64)))
    print("Antall noder med 128GB eller mer er: " + str(Regneklynge.noderMedNokMinne(abel, 128)))
    print("Antall prosessorer: " + str(Regneklynge.antProsessorer(abel)))
    print("Antall Rack: " + str(Regneklynge.getRacksNumber(abel)))
    
    
    
if __name__ == "__main__":
    main()