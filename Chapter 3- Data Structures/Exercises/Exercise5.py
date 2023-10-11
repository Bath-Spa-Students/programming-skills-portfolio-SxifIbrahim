## Exercise 5: Change Guest List

invitees = [
    {"name": "Mariez Cauyan", "message": "Dear Cauyan, I am truly fascinated by your groundbreaking contributions to physics and your profound insights into the nature of the universe. It would be an absolute honor to have you join me for dinner to discuss your theories, philosophy, and your remarkable journey through the world of science. Your presence would be inspiring beyond measure."},
    {"name": "Gwyneth Pastolero", "message": "Dear Pastolero, your poetry, literature, and your unwavering advocacy for civil rights have had a profound impact on countless lives, including mine. I would be deeply honored to share a meal with you, to hear your wisdom, and to learn from your experiences. Your words have touched hearts around the world, and I would be delighted to hear more of them in person."},
    {"name": "Alekzandra Balse", "message": "Dear Balse, your genius as a painter, scientist, and inventor has left an indelible mark on human history. Your insatiable curiosity and creativity have inspired generations. It would be an incredible privilege to have you as my guest for dinner, to discuss your incredible inventions and artistic masterpieces."}
]

guest_cant_make_it = "Mariez Cauyan"
print(f"{guest_cant_make_it} can't make it to the dinner.")

new_invitee = {"name": "Joshua Gofulco", "message": "Dear Madame Curie, your groundbreaking work in the field of radiology and your contributions to science..."}
invitees[0] = new_invitee

print("Second set of invitation messages:")
for invitee in invitees:
    print(f"Inviting {invitee['name']} to dinner:")
    print(invitee['message'])
    print("\n")