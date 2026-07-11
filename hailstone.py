# GitHub username: lopezram503
# Date: 7/10/26
# Description: This code starts with a positive number and follows the hailstone sequence rules.
# If the number is even, it is divided by 2.
# If thhe number is odd it is multiplied by 3 and then 1 is added.
# The code returns the total number of steps needed to reach 1.

def hailstone(start_number): # This line creates the hailstone function

    """Returns the number of steps needed to reach 1.""" # This line describes what the function does.

    if start_number == 1: # This line checks if the starting number is already 1.
        return 0 # This line returns 0 because no steps are needed.

    steps = 0 # This line starts counting the number of steps.

    while start_number != 1: # This loop continues until the starting number becomes 1.

        if start_number % 2 == 0: # This line checks if the starting number is even.

           start_number = start_number // 2 # This line divides the starting number by 2.

        else: # This line runs if the starting number is odd.

            start_number = start_number * 3 + 1 # This line multiplies the starting number by 3 adn adds 1.

        steps = steps + 1 # This line adds 1 to the total number of steps.

    return steps # This line tells us how many step it took.

# Tested the code using
# print(hailstone(3))








