## Exercise 6: Shrinking Guest List

invitees = ["Joshua Gofulco", "Gwyneth Pastolero", "Alekzandra Balse"]

print("Due to the change in plans, I can invite only two people for dinner.")

while len(invitees) > 2:
    removed_guest = invitees.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner this time.")

for invitee in invitees:
    print(f"{invitee}, you are still invited to dinner.")

del invitees[:]
print("\nFinal guest list:", invitees)