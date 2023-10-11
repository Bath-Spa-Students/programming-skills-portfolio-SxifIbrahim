## Exercise 7: Seeing the World

places_to_visit = ["Tokyo", "British Columbia", "Manila", "Seoul", "London"]

print("Original order:", places_to_visit)
print("Alphabetical order:", sorted(places_to_visit))
print("Original order (again):", places_to_visit)
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))
print("Original order (again):", places_to_visit)

places_to_visit.reverse()
print("Reversed order:", places_to_visit)
places_to_visit.reverse()
print("Original order (again):", places_to_visit)
places_to_visit.sort()
print("Alphabetical order (sorted):", places_to_visit)
places_to_visit.sort(reverse=True)
print("Reverse alphabetical order (sorted):", places_to_visit)
