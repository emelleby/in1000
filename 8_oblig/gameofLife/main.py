from spillebrett import Spillebrett as S

labels = S(2,2)
# Terminal Output
print()
for rad in labels._brett:
    for celle in rad:
        print(celle.hentStatusTegn(), end='')
    print("\n")

S.oppdatering(labels)

S.tegnBrett(labels)

print(labels._gen)

S.oppdatering(labels)

S.tegnBrett(labels)

print(labels._gen)