## Exercise 3: Glossary 2 :ballot_box_with_check:

"""
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 
to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
"""

glossary = {
    "Variable": "A named storage location in memory that can hold data.",
    "Loop": "A control structure that allows for repeated execution of a block of code.",
    "Function": "A reusable block of code that performs a specific task.",
    "Conditional Statement": "A statement that executes different code blocks based on a specified condition.",
    "List": "An ordered collection of elements, often of the same data type.",
    "Dictionary": "A collection of key-value pairs.",
    "Tuple": "An immutable ordered collection of elements.",
    "Boolean": "A data type representing True or False values.",
    "String": "A sequence of characters.",
    "Module": "A Python file containing reusable code and definitions."
}

for term, meaning in glossary.items():
    print(f"{term}:\n{meaning}\n")