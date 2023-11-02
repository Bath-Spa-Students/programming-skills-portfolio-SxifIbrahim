## Exercise 5: Cities

"""
Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, 
such as Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the default country.
"""

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

# Call the function for different cities and countries
describe_city("Abu Dhabi", "UAE")
describe_city("British Columbia", "Canada")
describe_city("Philippines") 
