"""
Write a Python program that uses a while loop to find the largest number among a series of
user-input values until they enter '0' to exit the loop.
"""

largest = None

while True:
    user_input = input("Enter a number (or '0' to exit): ")
    
    if user_input == '0':
        break
    
    try:
        number = float(user_input)
        if largest is None or number > largest:
            largest = number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if largest is not None:
    print(f"The largest number entered is: {largest}")
else:
    print("No valid numbers were entered.")