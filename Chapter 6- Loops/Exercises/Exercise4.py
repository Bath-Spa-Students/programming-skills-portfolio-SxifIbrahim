## Exercise 4: Deli

# Create a list of sandwich orders
sandwich_orders = ["Egg", "Roast Beef", "Grilled Cheese", "Ham", "Grilled Chicken"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Prepare and move each order to the finished sandwiches list
while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)