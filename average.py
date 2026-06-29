# Author: Ramiro Lopez
# GitHub username: lopezram503
# Date: 6/28/26
# Description: Asks the user for five numbers and
#              prints their average.

# Asks the user for five numbers.
print('Please enter five numbers.')


number_1 = float(input())
number_2 = float(input())
number_3 = float(input())
number_4 = float(input())
number_5 = float(input())

# Uses the five numbers entered to find the average.
average = (number_1 + number_2 + number_3 + number_4 + number_5) / 5

# Shows the average to the user.
print('The average of those numbers is:')
print(average)

