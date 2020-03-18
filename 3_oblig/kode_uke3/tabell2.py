tab = [ [5,3], [3,5] ]
rad1 = tab[0][0]+tab[0][1]
rad2 = tab[1][0]+tab[1][1]
kol1 = tab[0][0]+tab[1][0]
kol2 = tab[0][1]+tab[1][1]
alle_like = len(set([rad1,rad2,kol1,kol2]))==1
print(alle_like)
