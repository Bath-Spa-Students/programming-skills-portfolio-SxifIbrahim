"""
Given a Python list, write a program to remove all occurrences of item 20.
Given list:
 list1 = [5, 20, 15, 20, 25, 50, 20]
"""

list1 = [5, 20, 15, 20, 25, 50, 20]

# Remove all occurrences of item 20 using a list comprehension
list1 = [item for item in list1 if item != 20]

# Print the modified list
print(list1)