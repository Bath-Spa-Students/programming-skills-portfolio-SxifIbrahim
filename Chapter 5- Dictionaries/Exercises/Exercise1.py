## Exercise 1: Person :ballot_box_with_check:

"""
Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
"""

# Create a dictionary to store information about a person
person_info = {
    "first_name": "Seif",
    "last_name": "Ibrahim",
    "age": 18,
    "city": "Abu Dhabi"
}

# Print each piece of information stored in the dictionary
print("First Name: " + person_info["first_name"])
print("Last Name: " + person_info["last_name"])
print("Age: " + str(person_info["age"]))
print("City: " + person_info["city"])
