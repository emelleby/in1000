from spillebrett import Spillebrett as S

labels = S(3,3)
# Terminal Output
print()
for rad in labels._brett:
    for celle in rad:
        print(celle.hentStatusTegn(), end='')
    print("\n")