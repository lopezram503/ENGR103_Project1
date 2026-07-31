# GitHub username: lopezram503
# Date: 7/30/26
# Description: This code uses recursion to multiply two positive numbers by adding the first number
# as many times as the second number.


def multiply(first_number, second_number):

    """ Returns the product of two positive numbers using recursion."""

    # This line checks if the second number is 1
    if second_number == 1:

        # This line returns the first number and ends the recursion
        return first_number

    # This line adds the first number
    # Then it calls the function again using recursion
    # Then it reduces the second number by 1
    return first_number + multiply(first_number, second_number - 1)

