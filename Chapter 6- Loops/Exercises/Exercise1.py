## Exercise 1: Pizza Toppings

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
