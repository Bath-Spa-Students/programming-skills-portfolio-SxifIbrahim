## Exercise 5: Compute area of Circle :ballot_box_with_check:

""" 
Write a Python program which accepts the radius of a circle from the user and compute the area. 
"""
# Accept the radius from the user
pi = 3.14
r = float(input("Input the radius of the circle : "))

# Compute the area of the circle
calculatearea = str(pi * r**2);

# Print the result
print ("The area of the circle with radius " + str(r) + " is: " + calculatearea)