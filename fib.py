# GitHub username: lopezram503
# Date: 7/9/26
# Description: This code finds the Fiboanacci number at a given position.


def fib(position): # This line creates the fib function and accepts the position of the Fibonacci number to find.

    """Returns the Fibonacci number at the given position.""" # This line describes what the function does.

    if position == 1 or position == 2: # This line checks if the position is 1 or 2.
        return 1 # This line returns the value 1 if the position is 1 or 2.

    num_1 = 1 # This line stores the first Fibonacci number.

    num_2 = 1 # This line stores the second Fibonacci number.

    count = 3 # This line tells the program to begin finding Fibonacci numbers starting at position 3.

    while count <= position: # This line keeps the code running until it reaches the position entered by the user.

        result = num_1 + num_2 # This line adds the previous two numbers together.

        num_1 = num_2 # This line moves the second number into the first variable.

        num_2 = result # This line stores the new Fibonacci number.

        count = count + 1 # This line increases the counter by 1.

    return result # This line returns the Fibonacci number at the position entered by the user.

# Tested the function using
# term = fib(17)
# print(term)
# result: 1597

