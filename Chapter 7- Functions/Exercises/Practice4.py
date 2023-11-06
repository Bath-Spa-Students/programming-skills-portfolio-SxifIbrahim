"""
Write a Python program that defines a function to calculate the area of a circle, and then
calls that function with a given radius.
"""

import math

def calculate_circle_area(radius):
    if radius < 0:
        return None
    else:
        return math.pi * radius**2

# Input the radius
radius = float(input("Enter the radius of the circle: "))

# Call the function to calculate the area
area = calculate_circle_area(radius)

if area is not None:
    print(f"The area of the circle with radius {radius} is {area:.2f}")
else:
    print("Invalid input. Radius must be a non-negative number.")