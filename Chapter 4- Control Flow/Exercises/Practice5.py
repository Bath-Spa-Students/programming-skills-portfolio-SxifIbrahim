"""
Write a Python program that uses the elif statement to determine the season based on the
month provided as input.
"""

# Input the month from the user (assuming the input is an integer from 1 to 12)
month = int(input("Enter a month (1-12): "))

# Determine the season based on the input month
if 3 <= month <= 5:
    season = "Spring"
elif 6 <= month <= 8:
    season = "Summer"
elif 9 <= month <= 11:
    season = "Fall"
else:
    season = "Winter"

# Print the determined season
print(f"The season for month {month} is {season}.")