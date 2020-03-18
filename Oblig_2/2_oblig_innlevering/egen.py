#!usr/bin/env python3
# import to generate a random number in a range
import random

# Instruksjon
print("Gjett deg frem til heltallet")

# Generate a random number in a range 1-10
tall = random.randint(1,10)
# Cheating
# print(tall)

# Start a loop to ask for a guess until it is right
while(True):
    
    # Ask for a guess
    guess = int(input("Gjett på et tall mellom 1 og 10. "))
    
    # Check if it*s in range
    if guess > 10 or guess < 1:
        print(" Oi! Husk at det er et sted mellom og inkludert 1 og 10.")
    
    #If low
    elif guess < tall:
        print("Feil. Prøv et høyere tall: ")
    # If high
    elif guess > tall:
        print ("Feil. Prøv et lavere tall: ")
    
    # If perfect
    else:
        print("Perfekt! Du gjettet det.")
        # Exit loop
        break