## Exercise 4:  Large Shirts :ballot_box_with_check:

"""
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different message.
"""

def make_shirt(size='large', message='I love Reading Books'):
    print(f"Creating a {size} shirt with the message: {message}")

# Create a large shirt with the default message
make_shirt()

# Create a medium shirt with the default message
make_shirt(size='meduim')

# Create a small shirt with a custom message
make_shirt("Small", "I am a Book Worm!")