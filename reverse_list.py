# GitHub username: lopezram503
# Date: 8/6/26
# Description: This code changes the original list
# by reversing the order of its elements.


def reverse_list(element_list):

    """Reverses the order of the elements in the original list."""

    # Finds the last position in the list
    last_position = len(element_list) - 1

    # Starts at the beginning of the list and works towards the middle.
    for position in range(len(element_list) // 2):

        # Saves the current element before changing it.
        saved_element = element_list[position]

        # Moves the matching element from the end to the front.
        element_list[position] = element_list[last_position - position]

        # Places the saved element in the matching position at the end.
        element_list[ last_position - position] = saved_element








