#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 09:50:59 2020

@author: eivind
"""
from tkinter import *

root=Tk()



def name_and_alias(name,alias):
    return name.strip().title() + ':' + alias.strip().title()

name_and_alias1 = lambda name,alias: name.strip().title() + ':' + alias.strip().title()

def name_and_alias2(name,alias): return name.strip().title() + ':' + alias.strip().title()


x= name_and_alias(' john    ClEEse  ','HECKLER')

# print(name_and_alias1(' john   ClEEse  ','HECKLER'))

# print(name_and_alias2(' john    ClEEse  ','HECKLER'))

myLabel = Label(root, text="Hello, World!")
myLabel.grid(row=0,column=0)
root.mainloop()