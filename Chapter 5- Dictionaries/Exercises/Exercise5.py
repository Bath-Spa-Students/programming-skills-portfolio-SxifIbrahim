## Exercise 5: Pets

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
