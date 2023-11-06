"""
Write a python program with if statement that assigns 20 to the variable y and assigns 40 to the
variable z if the variable & is greater than 100.
"""

num = 101  # Replace this with the actual value of &

if num > 100:
    y = 20
    z = 40
else:
    y = z = 0  # Assign default values when & is not greater than 100

# Print the values of y and z
print(f"y: {y}")
print(f"z: {z}")
