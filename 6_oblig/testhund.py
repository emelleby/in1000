#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:40:22 2020

@author: eivind
"""
from hund import Hund as H

def main():
    
    fido = H(3, 10)

    print(fido)
    
    fido.spis(3)
    
    print(fido)
    
    fido.spring()
    
    # Slik som dette skal man altså ikke gjøre.
    print(fido._vekt)
    fido._vekt += 12
    print(fido._metthet)
    fido.spis(1)
    print(fido._metthet)

    print("SLIK skal det gjøres..")
    print(fido.hentVekt(), "kilo")
    print(fido.hentAlder(), 'år')
    
    fido.spring()
    fido.spring()
    
    print(fido)
    
    fido.spis(4)
    
    print(fido)


if __name__ == "__main__":    
    main()