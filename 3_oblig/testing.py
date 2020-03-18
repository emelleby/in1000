liste = [1, 2, 3]
l = len(liste)
""" Function to calculate the product of the numbers in the list
def produkt(liste):
    produkt_liste = 1
    for i in range(len(liste)):
        produkt_liste *= liste[i]
    return produkt_liste
    
def produkt(liste):
    produkt = 1
    for i in liste:
        produkt *= i
    return produkt

print(produkt(liste))

def multiplyList(l, i):
    if i == 0:
        print("ett tall")
        return = l[i]
    return l[i] * multiplyList(l[i - 1])
"""
# Recursive Python3 code 
# to multiply array elements 

# Function to calculate the product 
# of array using recursion 
def multiply( a , n ): 
	
    # Termination condition 
    if n == 0: 
        return(a[n]) 
    else: 
        return (a[n] * multiply(a, n - 1))

# Driver Code 
# array = [1, 2, 3, 4, 5, 6] 
# n = len(array) 

# Function call to 
# calculate the product
print("product is:")
print(multiply(liste, len(liste) - 1)) 

