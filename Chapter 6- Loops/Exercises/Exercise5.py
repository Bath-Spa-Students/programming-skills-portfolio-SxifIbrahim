## Exercise 5: No Pastrami :ballot_box_with_check:

"""
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 
occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
"""

# Create a list of sandwich orders
sandwich_orders = [
    'pastrami', "Egg", "Roast Beef", "Grilled Cheese", "Ham", "Grilled Chicken"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Check for pastrami and remove it from sandwich orders
print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")

# Process sandwich orders and move them to the list of finished sandwiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")