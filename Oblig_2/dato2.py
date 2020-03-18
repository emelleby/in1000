#!/usr/bin/env python3
# Ask for date1 as a mmdd & store as int
date1 = int(input("Angi dato 1 på formen 'mmdd': "))

# Ask for date2 as a mmdd & store as int
date2 = int(input("Angi dato 2 på formen 'mmdd': "))

# Check if date1 is less than date2
if (date1 < date2):
    print("Riktig rekkefølge!")

# Check if same day and month
elif (date1 == date2):
    print("Samme dato!")

# if none of the above then it comes after
else:
    print("Feil rekkefølge!")
