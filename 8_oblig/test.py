#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:56:23 2020

@author: eivind
"""
class Tablecheck:
    def __init__(self):
        self._grid = [['A','B','C'] ,
                      ['D','E','F'] ,
                      ['G','H','I'] ,
                      ['J','K','L']]
                      
    
    def print_grid(self):
        for row in self._grid:
            print (row)

    def finnNabo(self, cellerad, cellekolonne):
        # definer søkeområdet
        search_min = -1
        search_max = 2

        naboliste = []
        print("len(self._grid[0]: " + str(len(self._grid[0])))
        print("len(self._grid: " + str(len(self._grid)))
        # sjekk naboer start med -1, -1 - Hvis det er 'E' så vil det være 'A'
        # start med første rad i matrisen
        for rad in range(search_min, search_max):
            # start med første kolonne på den raden og ta en og en celle bortover
            for kolonne in range(search_min, search_max):
                naborad = rad + cellerad
                nabokolonne = kolonne + cellekolonne

                # Sjekk om nabocellen er utenfor matrisen (West, North)
                if (naborad or nabokolonne) < 0:
                    continue
                # Sjekk om nabocellen er utenfor matrisen (East, South)
                if naborad >= len(self._grid) or nabokolonne >= len(self._grid[0]):
                    continue

                # Sjekk om cellen er sin egen
                elif naborad == cellerad and nabokolonne == cellekolonne:
                    continue
                
                # Ellers legges cellen til nabolisten
                else:
                    naboliste.append((naborad, nabokolonne))

        return naboliste
                    
                

def main():
    table1 = Tablecheck()
    table1.print_grid()
    print(table1.finnNabo(3,2))

    x=table1.finnNabo(3,2)
    for x,y in x:
        print(table1._grid[x][y], end=', ')

if __name__ == "__main__":

    main()

