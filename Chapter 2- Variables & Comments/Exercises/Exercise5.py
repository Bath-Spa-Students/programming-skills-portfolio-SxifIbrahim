## Exercise 5: USB Shopper :ballot_box_with_check:

""" 
    A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
    Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
    You will to use the arithmetic operators to complete this exercise. 
"""

# Total USB Sticks
usb = 6

# Price of USB Sticks
budget = 50

# Calculate the number of USB sticks she can buy
usb_bought = budget // usb

# Calculate how many pounds she will have left
change = budget % usb_bought

# Print the Result
print (f"She bought {usb_bought} and will still have {change} pounds left.")