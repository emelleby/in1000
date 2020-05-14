#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:10:24 2020

@author: eivind
"""

class Fish:
    def __init__(self, first_name, last_name="Fish",
                 skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
        
    def __str__(self):
        return f"Firstname: {self.first_name}\nLastname: {self.last_name}\nSkeleton: {self.skeleton}\nEyelids: {self.eyelids}"

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")
        
class Shark(Fish):
    def __init__(self, first_name, last_name="Shark",
                 skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")
        
class Trout(Fish):
    def __init__(self, water = "freshwater"):
        self.water = water
        super().__init__(self)
        
    def __str__(self):
        return f"Firstname: {self.first_name}\nLastname: {self.last_name}\nEyelids: {self.eyelids}\nWater: {self.water}"
        
terry = Trout()
# Then you need to initialize the other attributes of Parent class 'Fish'
terry.first_name = "Terry"
# Before you print or anything
print(terry)
print()
lars=Fish("Lars")
print(lars)
print()
finn=Shark("Finn")
print(finn)