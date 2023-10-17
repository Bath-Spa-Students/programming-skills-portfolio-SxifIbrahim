## Exercise 3: Glossary 2

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