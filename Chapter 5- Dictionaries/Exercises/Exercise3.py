## Exercise 3: Glossary 2

glossary = {
    "Variable": "A named storage location in memory that can hold data.",
    "Loop": "A control structure that allows for repeated execution of a block of code.",
    "Function": "A reusable block of code that performs a specific task.",
    "Conditional Statement": "A statement that executes different code blocks based on a specified condition.",
    "List": "An ordered collection of elements, often of the same data type."
}

# Print each word and its meaning with neat formatting
for term, meaning in glossary.items():
    print(f"{term}:\n{meaning}\n")