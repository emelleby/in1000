#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:36:58 2020

@author: eivind
"""
def openToList(filename):
    """
    Function to open a file and it takes the filename as an argument
    """
    inn = open(filename, mode = "r+", encoding='utf-8-sig')
    liste =[]
    for linje in inn:
        liste.append(linje.strip())
    inn.close()
    return liste

"""
import csv
def openToList(filename):
    with open(filename, mode = "r+",  newline='', encoding='utf-8-sig') as inn:
        data = csv.reader(inn)
        liste = [data]
#        for linje in data:
#            liste.append(linje.strip())
        inn.close()
        return liste


lineCount = 0
innFil = openToList("./Resultlist-47130.csv")
linjer = []
for linje in innFil:
    lineCount += 1
    biter = linje.split(';')
    #biter.strip('\"')
    linjer.append(biter)

# Remove all double quotes
for linje in linjer:
    for biter in linje:
        biter.replace('"', '')
        
        
test = '"tull"'
print(test)
test.strip('\"')
print(test)
print(linjer[0][0])
"""

lineCount = 0
innFil = openToList("Resultlist-2.csv")
linjer = []
for linje in innFil:
    lineCount += 1
    biter = linje.split(';')
    linjer.append(biter)
    
    
# Definer en liste av klasser
classes = []

# Les in alle oppføringer i kolonne 9 som er klasser
for linje in linjer:
    classes.append(linje[8])

# Lag et set av listen for å ha kun unike verdier
klasser = set(classes)
klasser.remove("Class")

# print(sorted(klasser))

print("Tilgjengelige klasser i skirennet er: \n")

# Definer en dictionary med resultatene fra løkken
onskeDict = {}
# Presenter alle klassene med et nummer som vil tilkjennegi klassen for brukeren.
for index, klasse in enumerate(sorted(klasser)):

    # Assosier nummer med klasse i ordlisten
    onskeDict[index + 1] = klasse
    print(f"{index + 1:<2}  |  {klasse}")

# print(onskeDict)
    
onske = input("Hvilken klasse vil du se? ")

# Define a function to make a list of the preferred class to be viewed.
def printResultat(data, ordListe, onske):
    klasse = []
    # For hver linje i datasettet sjekk om index 8 er lik valget som er lagret i ordlisten.
    for linje in data:
        # Hvis det er tilfellet, legg den linjen inn i listen.
        if linje[8] == ordListe.get(int(onske), 1):
            klasse.append(linje)

    return klasse

print("Dessverre er det litt rot i datagrunnlaget.") if onske == "1" else print(f"Resultatene for klasse {onskeDict.get(int(onske), 1)}:\n")

# Make a list of the class asked for
klasseResultat = printResultat(linjer,onskeDict,onske)

# Print the wanted information in a formatted way
# print(f"Resultatene for klasse {onskeDict.get(int(onske), 1)}:\n")
print(f"{linjer[0][0]:<5} | {linjer[0][2]:<25} | {linjer[0][3]:<20} | {linjer[0][9]:<14}")
for i, result in enumerate(klasseResultat):
    print(f"{result[0]:<5} | {result[2]:<25} | {result[3]:<20} | {result[9]:<14}")
    
