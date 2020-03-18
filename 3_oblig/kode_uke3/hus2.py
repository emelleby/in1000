kast = [3,3,4,3,3]
ulike = set(kast)
hus_eller_4like = len(ulike)==2

en_terning = kast[0]
antall = kast.count(en_terning)
ikke4like = (antall==2 or antall==3)

print(hus_eller_4like and ikke4like)
