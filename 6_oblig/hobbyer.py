#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:30:05 2020

@author: eivind
"""

class Person:
    def __init__(self,navn,alder):
        self.navn = navn
        self.alder = alder
        self.hobbyer = []

    def leggTilHobby(self, hobby):
        self.hobbyer.append(hobby)

    def skrivHobbyer(self):
        hobbies = ""
        for hobby in self.hobbyer:
            hobbies += hobby + ", "
        return hobbies

    def skrivUtsom(self):
        return f"{navn}({alder}) har følgende hobbyer: " + Person.skrivHobbyer(self)
       

navn = input('Hva er ditt navn? ')
alder = input('Hvor gammel er du? ')

bruker = Person(navn, alder)

#hobby = None
hobby = input("Har du en hobby? ").lower()

while hobby != "nei":
    
    Person.leggTilHobby(bruker, hobby.capitalize())
    print("Har du flere hobbier? ")
    hobby = input("Hobby eller 'nei' om du vil slutte. ").lower()
        
else:
    print(Person.skrivUtsom(bruker))

        

        