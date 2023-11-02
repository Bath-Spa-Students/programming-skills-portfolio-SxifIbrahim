## Exercise 3: Print date and Time :ballot_box_with_check:

""" 
Write a Python program to display the current date and time. 
"""

import datetime

# Get the Current Date and Time
now = datetime.datetime.now()
print ("Current date and time : ")

# Print the Date and Time
print (now.strftime("%Y-%m-%d %H:%M:%S"))   