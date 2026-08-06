# GitHub username: lopezram503
# Date: 8/5/26
# Description: This function goes through a list of numbers and replaces
# each number with the square of that number.


def square_list(number_list):
    """Replace every number in the list with its square."""

    # Goes through each position in the list and changes each number to its square.
    for position in range(len(number_list)):

        # Replaces the number with the square of that number.
        number_list[position] = number_list[position] * number_list[position]


