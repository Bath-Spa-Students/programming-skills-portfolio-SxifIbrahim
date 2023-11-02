## Exercise 4: Rivers :ballot_box_with_check:

"""
Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
* Use a loop to print the name of each river included in the dictionary.
* Use a loop to print the name of each country included in the dictionary.
"""

# Create a dictionary of rivers and the countries they run through
rivers = {
    "Congo": "Africa",
    "Ganges": "India",
    "Mississipi": "Brazil"
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# Print the names of each river
print("\nRivers:")
for river in rivers:
    print(river)

# Print the names of each country
print("\nCountries:")
for country in rivers.values():
    print(country)
