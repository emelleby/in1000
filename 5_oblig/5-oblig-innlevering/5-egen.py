#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:36:58 2020

@author: eivind melleby

Programmet laster inn en csv fil med resultater fra et skirenn. 
Programmet viser hvilke klasser som har vært med og tilbyr å vise resultater 
for en valgt klasse.
"""

def openToList(filename):
    """
    Function to open a file and it takes the filename as an argument
    """
    inn = open(filename, mode = "r", encoding='utf-8-sig')
    liste =[]
    for linje in inn:
        liste.append(linje.strip())
    inn.close()
    return liste

# Åpne en fil med funksjonen 'openToList'
innFil = openToList("Resultlist-6.csv")

# Definer en ny liste
linjer = []

# Del hver linje opp i lister
for linje in innFil:
    biter = linje.split(';')
    linjer.append(biter)
    
    
# Definer en liste av klasser
classes = []

# Les in alle oppføringer i kolonne 9 som er klasser
for linje in linjer:
    classes.append(linje[8])

# Lag et set av listen for å ha kun unike verdier
klasser = set(classes)
# Fjern overskriften
klasser.remove("Class")


print("Tilgjengelige klasser i skirennet er: \n")

# Definer en dictionary med resultatene fra løkken under
onskeDict = {}
# Presenter alle klassene med et nummer som vil tilkjennegi klassen for brukeren.
for index, klasse in enumerate(sorted(klasser)):

    # Assosier nummer med klasse i ordlisten
    onskeDict[index + 1] = klasse
    print(f"{index + 1:<2}  |  {klasse}")

# Be brukeren om hvilken klasse man vil se.    
onske = input("Hvilken klasse vil du se? ")

def getClass(data, ordListe, onske):
    """
    Function to make a list of the preferred class to be viewed.
    The function takes a nested list of results, the dictionary of classes 
    and the choice of class as arguments.
    It will return a list object 
    """
    
    # Ny liste for lagring av den aktuelle klassen
    klasse = []
    # For hver linje i datasettet sjekk om index 8 er lik valget som er lagret i ordlisten.
    for linje in data:
        # Hvis det er tilfellet, legg den linjen inn i listen.
        if linje[8] == ordListe.get(int(onske), 1):
            klasse.append(linje)

    return klasse

# print("Dessverre er det litt rot i datagrunnlaget.") if onske == "1" else \
print(f"\nResultatene for klasse {onskeDict.get(int(onske))}:\n")

# Make a list of the class asked for
klasseResultat = getClass(linjer,onskeDict,onske)

# Print the wanted information in a formatted way
# print(f"Resultatene for klasse {onskeDict.get(int(onske), 1)}:\n")
print(f"{linjer[0][0]:<6} | {linjer[0][2]:<25} | {linjer[0][3]:<20} | {linjer[0][9]:<14}")
for i, result in enumerate(klasseResultat):
    print(f"{result[0]:<6} | {result[2]:<25} | {result[3]:<20} | {result[9]:<14}")
    
