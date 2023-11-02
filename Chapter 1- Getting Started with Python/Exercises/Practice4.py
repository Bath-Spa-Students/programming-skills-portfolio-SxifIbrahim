"""
Compute the area of a triangle
"""

# Input the base and height of the triangle
base = float(input("Enter the length of the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area of the triangle
area = (base * height) / 2

# Print the result
print(f"The area of the triangle is {area:.2f}")