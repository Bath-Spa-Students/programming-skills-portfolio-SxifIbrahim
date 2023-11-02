## Exercise 3: Stripping Names :ballot_box_with_check:

""" 
Tidy up the code to make it easier to understand
Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, 
“\t” and “\n”, at least once. Print the name once, so the whitespace around the name is displayed. 
Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip(). 
"""

# Define a person's name with whitespace characters
name = "\t   Hannah Mei Gwyneth Pastolero\n"

# Print the name with whitespace
print("Name with whitespace: ", name)

# Strip whitespace from the left (left-justified)
print("Name after lstrip():", name.lstrip())

# Strip whitespace from the right (right-justified)
print("Name after rstrip():", name.rstrip())

# Strip whitespace from both ends
print("Name after strip():", name.strip())
