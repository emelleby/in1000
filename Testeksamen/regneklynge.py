#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 10:17:02 2020

@author: eivind
"""

from node import Node
from rack import Rack

class Regneklynge():
    """
    Klassen Regneklynge tar imot en node og plasserer den i et rack
    """
    def __str__(self):
        return f"Regneklyngen {self._navn} har {len(self._racks)} racks."
    
    def __init__(self, antNoder, navn):
        
        # Tips. Det kan være lurt å ta inn antall noder per rack i konstruktøren til Regneklynge.
        self._antNoder = antNoder
        self._navn = navn
        
        #liste som holde racks i klyngen
        self._racks = []
        
    def nyRack(self):
        """ Oppretter et nytt Rack """
        self._racks.append(Rack(self._antNoder))
    
    def nyNode(self, ram, cpu):
        # Hvis det ikke er noen rack opprettes et
        if not self._racks:
            self.nyRack()
            
        # metode som tar imot et nodeobjekt og plasserer det i et rack med ledig plass.
        
        # print(self._racks)
        # det er plass i et rack plasseres det der.
        if not Rack.fulltRack(self._racks[-1]):
            Rack.leggTilNode(self._racks[-1], ram, cpu)
            
        else:
            self.nyRack()
            Rack.leggTilNode(self._racks[-1], ram, cpu)
                
            # Hvis alle rackene er fulle opprettes et nytt
    
    #, skal det lages et nytt Rack-objekt som legges inn i listen, 
    # og noden plasseres i det nye racket.
    def getRacksNumber(self):
        return len(self._racks)
    
    def getRack(self, index):
        return self._racks[index]
    
    def antProsessorer(self):
        """
        returnerer det totale antall prosessorer i regneklyngen.
        """
        prosessorer = 0
        
        # Iterer listen av racks
        for rack in self._racks:
            # hent listen med noder i det aktuell racket
            noder = rack.getNoder()
            # Gå igjennom listen av noder i racket
            for node in noder:
                # Legg till antallet prosessorer for hver node til totalen
                prosessorer += Node.getNode(node)[1]
        # returner det totale antallet prosessorer        
        return prosessorer
                

    def noderMedNokMinne(self, paakrevdMinne):
        """
        returnerer det totale antall noder med nok påkrevd minne i regneklyngen.
        """
        noderMedMinne = 0
        
        # Iterer listen av racks
        for rack in self._racks:
            # hent listen med noder i det aktuell racket
            noder = rack.getNoder()
            # Gå igjennom listen av noder i racket
            for node in noder:
                # Hvis det er nok minne i noden legg til 1
                if Node.getNode(node)[0] >= paakrevdMinne:
                # Legg till antallet prosessorer for hver node til totalen
                    noderMedMinne += 1
        # returner det totale antallet prosessorer        
        return noderMedMinne
        
        
        
        
        