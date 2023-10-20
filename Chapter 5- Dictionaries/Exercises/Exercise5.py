## Exercise 5: Pets :ballot_box_with_check:

"""
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
owner's name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 
each pet.
"""

pets = [
    {"kind": "Dog", "owner": "Mairez"},
    {"kind": "Cat", "owner": "Seif"},
    {"kind": "Fish", "owner": "Gwyneth"},
    {"kind": "Parrot", "owner": "Joshua"},
]

for pet in pets:
    print(f"Kind of animal: {pet['kind']}")
    print(f"Owner's name: {pet['owner']}")
    print()
