## Exercise 4: Guest List :ballot_box_with_check:

""" 
If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d
like to invite to dinner. Then use your list to print a message to each person, invitingthem to dinner. 
"""

invitees = [
    {"name": "Mariez Cauyan", "message": "Dear Cauyan, I am truly fascinated by your groundbreaking contributions to physics and your profound insights into the nature of the universe. It would be an absolute honor to have you join me for dinner to discuss your theories, philosophy, and your remarkable journey through the world of science. Your presence would be inspiring beyond measure."},
    {"name": "Gwyneth Pastolero", "message": "Dear Pastolero, your poetry, literature, and your unwavering advocacy for civil rights have had a profound impact on countless lives, including mine. I would be deeply honored to share a meal with you, to hear your wisdom, and to learn from your experiences. Your words have touched hearts around the world, and I would be delighted to hear more of them in person."},
    {"name": "Alekzandra Balse", "message": "Dear Balse, your genius as a painter, scientist, and inventor has left an indelible mark on human history. Your insatiable curiosity and creativity have inspired generations. It would be an incredible privilege to have you as my guest for dinner, to discuss your incredible inventions and artistic masterpieces."}
]

for invitee in invitees:
    print(f"Inviting {invitee['name']} to dinner:")
    print(invitee['message'])
    print("\n")
