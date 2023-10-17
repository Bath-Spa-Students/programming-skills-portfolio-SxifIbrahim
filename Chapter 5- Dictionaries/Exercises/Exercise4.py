## Exercise 4: Rivers

rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China"
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nRivers:")
for river in rivers:
    print(river)

print("\nCountries:")
for country in rivers.values():
    print(country)
