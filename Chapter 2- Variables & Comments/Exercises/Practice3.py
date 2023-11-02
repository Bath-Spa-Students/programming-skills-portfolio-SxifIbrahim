"""
Write a python program that takes an input 5 from user and then type cast those values to string, int
and float in the separate variables. Print all the variables.
"""

# Take an input from the user
user_input = input("Pick a Number: ")

# Typecast the input to string, int, and float
input_string = str(user_input)
input_int = int(user_input)
input_float = float(user_input)

# Print all the variables
print(f"Original: {user_input}")
print(f"String: {input_string}")
print(f"Int: {input_int}")
print(f"Float: {input_float}")