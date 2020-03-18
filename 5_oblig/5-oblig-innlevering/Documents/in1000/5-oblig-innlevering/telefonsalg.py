#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:52:48 2020

@author: eivind
"""

def innlesning(filnavn):
    """
    Funksjon som tar en fil med 2 verdier separert med mellomrom som parameter og legger linjene in i en ordbok.
    Funksjonen konerterer element 2 paa hver linje til heltall.
    Ordboken returneres
    """

    ordbok = {}
    innfil = open(filnavn, mode='r')
    for linje in innfil:
        biter = linje.split(' ')
        ordbok[biter[0]] = int(biter[1])

    # Lukk filen
    innfil.close()
    return ordbok


# innlesning("salgstall.txt")

"""Lag en prosedyre maanedensSalgsperson som tar imot en ordbok, går gjennom denne og skriver ut navn og antall salg for den personen som solgte mest den måneden."""

def maanedensSalgsperson(ordbok):
    """
    Function that will take a dict as argument and prints a sorted list
    by value in reverse order.
    It create a list of tuples and print the index 0 and the length of the list.
    """
    for key, value in sorted(ordbok.items(), reverse=True, key=lambda x: x[1]):
        print(f"Navn: {key:<5} - Salg: {value}")
   
    print('')

    # Create a list of tuples sorted by index 1 i.e. value field     
    listofTuples = sorted(ordbok.items(), reverse=True, key=lambda x: x[1])
    print(f"Maanedens salgsperson er {listofTuples[0][0]} med {listofTuples[0][1]} salg.\n")
    print(f"Aktive selgere denne perioden er {len(listofTuples)}.")


def totaltAntallSalg(ordbok):
    """3. Skriv en funksjon totaltAntallSalg som tar imot en ordbok og returnerer summen av innholdsverdiene i ordboken."""
    total = 0
    for salg in ordbok.values():
        total += salg

    return total


def gjennomsnittSalg(ordbok):
    total = 0
    for i, salg in enumerate(ordbok.values()):
        total += salg

    return round(total / (i + 1), 2)
assert gjennomsnittSalg({'foo': 2.34, 'baz': 4.56, 'bar': 9.21}) == 5.37
# print(gjennomsnittSalg(x))

"""Til slutt skal du skrive en prosedyre hovedprogram(). Inne i hovedprogram skal du skrive ut den faktiske statistikken. Bruk funksjonene og prosedyrene du har laget, og skriv i tillegg ut antall selgere som ble lest inn. Filen du skal bruke for å teste programmet ditt er salgstall.txt. Denne txt.-filen skal leveres sammen med resten av filene på Devilry."""

def hovedprogram(fil):
    salgstall = innlesning(fil)
    print("Salgstallene for perioden er:")
    maanedensSalgsperson(salgstall)
    print(f"Totalt antall salg: {totaltAntallSalg(salgstall)}")
    print(f"Gjennomsnittlig salg er: {gjennomsnittSalg(salgstall)}")
    
    

hovedprogram("salgstall.txt")




