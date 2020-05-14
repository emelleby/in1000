#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:56:09 2020

@author: eivind
"""

def erstatt(argument):
    bok = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return bok.get(1, "Ugyldig måned")

if __name__ == "__main__":    
    print(erstatt(1))