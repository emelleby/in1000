# Ask for day1 & store as int
day1 = int(input("Angi dag 1: "))

# Ask for month1 & store as int
month1 = int(input("Angi måned 1: "))

# Ask for day2 & store as int
day2 = int(input("Angi dag 2: "))

# Ask for month2 & store as int
month2 = int(input("Angi måned 2: "))

# Check if month1 is less than month2 
if (month1 < month2):
    print("Riktig rekkefølge!")

# Check if day1 is less than day2 if same month 
elif (month1 == month2 and day1 < day2):
    print("Riktig rekkefølge!")

# Check if same day and month
elif (month1 == month2 and day1 == day2):
    print("Samme dato!")

# if none of the above then it's wrong
else:    
    print("Feil rekkefølge!")