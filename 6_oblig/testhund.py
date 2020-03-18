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
    
    print(fido.vekt)
    print(fido.metthet)
    fido.spis(1)
    print(fido.metthet)
    print(fido.vekt)
    
    fido.spring()
    fido.spring()
    
    print(fido)
    
    fido.spis(4)
    
    print(fido)


if __name__ == "__main__":    
    main()