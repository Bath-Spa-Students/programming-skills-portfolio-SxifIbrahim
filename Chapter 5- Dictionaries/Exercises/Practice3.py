"""
Write a Python program to iterate through the values of a dictionary and print them.
"""

# Create a sample dictionary
my_dict = {
    "name": "Seif",
    "age": 18,
    "city": "Abu Dhabi",
    "email": "sibrahim.rtei@email.com"
}

# Iterate through the values and print them
for key in my_dict:
    value = my_dict[key]
    print(value)