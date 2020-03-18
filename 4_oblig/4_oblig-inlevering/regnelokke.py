"""
Programmet går noen runder med seg selv.
"""
x = []
while 0 not in x:
    x.append(int(input()))

for tall in x:
    print(tall)

minSum = 0

for tall in x:
    minSum += tall

print(minSum)