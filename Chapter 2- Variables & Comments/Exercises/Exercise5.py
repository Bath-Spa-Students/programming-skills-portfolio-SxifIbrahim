## Exercise 5: USB Shopper :ballot_box_with_check:

""" 
A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
You will to use the arithmetic operators to complete this exercise. 
"""

usb = 6
budget = 50

usb_bought = budget // usb
change = budget % usb_bought

print (f"She bought {usb_bought} and will still have {change} pounds left.")