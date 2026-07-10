# GitHub username: lopezram503
# Date: 7/9/26
# Description: This code will help us calculate the distance an object falls
# due to gravity using the formula: d = (1/2) * g * time^2, where g = 9.8 m/s^2.

# This line starts the fall_distance function.
def fall_distance(time):

    # This line explains what the fall_distance function does.
    """Returns the distance an object falls due to gravity."""

    # This line calculates the distance using the formula.
    dist = (1 / 2) * 9.8 * time **2

    # This line returns the calculated distance.
    return dist

# Tested the function using
#print(fall_distance(3.2))
# and got 50.176000000000016