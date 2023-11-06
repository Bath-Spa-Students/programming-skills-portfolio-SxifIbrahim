"""
Write a Python program to merge two dictionaries into one.
"""

# Define two dictionaries
dict1 = {"name": "Seif", "age": 18}
dict2 = {"city": "Abu Dhabi", "email": "sibrahim.rtei@email.com"}

# Merge the dictionaries into a new dictionary
merged_dict = {**dict1, **dict2}

# Print the merged dictionary
print("Merged Dictionary:")
print(merged_dict)
