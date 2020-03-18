tab = [ [5,3], [3,5] ]
rad1 = tab[0][0]+tab[0][1]
rad2 = tab[1][0]+tab[1][1]
kol1 = tab[0][0]+tab[1][0]
kol2 = tab[0][1]+tab[1][1]
alle_like = rad1==rad2 and rad1==kol1 and rad1==kol2
print(alle_like)
