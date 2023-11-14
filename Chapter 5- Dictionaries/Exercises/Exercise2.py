## Exercise 2: Glossary :ballot_box_with_check:

"""
A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 
their meanings as values.
* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 
the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 
each word-meaning pair in your output.
"""

# Create a glossary (dictionary) of programming terms and their meanings    
glossary = {
    "Variable": "A named storage location in memory that can hold data.",
    "Loop": "A control structure that allows for repeated execution of a block of code.",
    "Function": "A reusable block of code that performs a specific task.",
    "Conditional Statement": "A statement that executes different code blocks based on a specified condition.",
    "List": "An ordered collection of elements, often of the same data type."
}

# Print each word and its meaning with a newline character between them
print("Variable:\n", glossary['Variable'],  "\n")
print("Loop:\n", glossary['Loop'],  "\n")
print("Function:\n", glossary['Function'],  "\n")
print("Conditional Statement:\n", glossary['Conditional Statement'],  "\n")
print("List:\n", glossary['List'],  "\n")