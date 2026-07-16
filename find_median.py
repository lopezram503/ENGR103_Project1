# GitHub username: lopezram503
# Date: 7/15/26
# Description: This code finds the statistical median of a list of numbers.
# The list is sorted from smallest to largest before calculating the median.
# It returns the middle number for lists with an odd number of values and
# returns the average of the two middle numbers for lists with an even
# number of values.


def find_median(num_list): # This line creates the find_median function and accepts a list of numbers.

    """Returns the statistical median number from a list of numbers."""

    sorted_list = sorted(num_list) # This line sorts the list from smallest to largest.

    number_of_values = len(sorted_list) # This line stores the number of values in the list.

    if number_of_values % 2 == 1: # This line checks if the list has an odd number of values.

        middle_index = number_of_values // 2 # This line finds the middle position.

        return sorted_list[middle_index] # This line returns the middle number.

    else: # This line runs if the list has an even number of values.

        right_middle = number_of_values // 2 # This line finds the second middle position.

        left_middle = right_middle - 1 # This line finds the first middle position.

        left_number = sorted_list[left_middle] # This line stores the first middle number.

        right_number = sorted_list[right_middle] # This line stores the second middle number.

        return (left_number + right_number) / 2 # This line returns the average of the two middle numbers.












