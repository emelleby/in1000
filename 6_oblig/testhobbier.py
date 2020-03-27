#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:30:05 2020

@author: eivind
"""
from hobbyer import Person

def main():
    navn = input('Hva er ditt navn? ')
    alder = input('Hvor gammel er du? ')

    bruker = Person(navn, alder)

    #hobby = None
    hobby = input("Har du en hobby? ").lower()

    while hobby != "nei":
        
        bruker.leggTilHobby(hobby.capitalize())
        print("Har du flere hobbier? ")
        hobby = input("Hobby eller 'nei' om du vil slutte. ").lower()
            
    else:
        print(bruker.skrivUtsom())

if __name__ == "__main__":
    main()   