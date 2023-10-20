## Exercise 1: Pizza Toppings :ballot_box_with_check:

"""
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""

toppings = []

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping == 'quit':
        break
    
    print(f"I'll add {topping} to your pizza.")
    toppings.append(topping)

if toppings:
    print("You've chosen the following pizza toppings:")
    for topping in toppings:
        print(topping)
else:
    print("You didn't select any pizza toppings.")
