# GitHub username: lopezram503
# Date: 7/16/26
# Description: This code creates a new list with repeated values removed
# while keeping the original order of the values.

# This line creates the without_duplicates function and accepts a list.
def without_duplicates(my_list):
    """Returns a new list with repeated values removed."""

    # This line creates an empty list.
    new_list = []

    # This loop goes through each value in the list.
    for value in my_list:

        # This line checks if the value has not already been added.
        if value not in new_list:

            # This line adds the value to the new list.
            new_list.append(value)

    # This line returns the new list.
    return new_list


