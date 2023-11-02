## Exercise 6: Shrinking Guest List :ballot_box_with_check:

"""
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting 
them know you’re sorry you can’t invite them to dinner.
•Print a message to each of the two people still on your list, letting them know they’re still invited.
•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
"""

# Create a list of people to invite to dinner
invitees = ["Joshua Gofulco", "Gwyneth Pastolero", "Alekzandra Balse"]

# Print an invitation message for each person
for person in invitees:
    print(f"Dear {person}, I would like to invite you to dinner.")

print("\nSorry, the dinner table won't arrive in time, and I can only invite two people.\n")

# Use pop() to remove guests from the list and apologize to them
while len(invitees) > 2:
    removed_guest = invitees.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Print an invitation message for the two remaining guests
for person in invitees:
    print(f"Dear {person}, you're still invited to dinner.")

# Use del to remove the last two names from the list
del invitees[:]
print("\nThe list of guests is now empty:", invitees)
