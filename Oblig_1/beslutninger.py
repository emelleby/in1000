# print question
print("Vil du ha en brus?")

# Ask for input
answer = input()

# if user answers "ja" print out
if(answer == "ja"):
    print("Her har du en brus!")

# if user answers "nei" print out
elif(answer == "nei"):
    print("Den er grei.")

# if user answers "whatever else" print out
else:
    print("Det forstod jeg ikke helt.")