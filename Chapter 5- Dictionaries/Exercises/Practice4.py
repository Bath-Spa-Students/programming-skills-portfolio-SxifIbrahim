"""
Write a Python program to iterate through both the keys and values of a dictionary and print
them 
"""

# Create a sample dictionary
my_dict = {
    "name": "Seif",
    "age": 18,
    "city": "Abu Dhabi",
    "email": "sibrahim.rtei@email.com"
}

# Iterate through both keys and values and print them
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")