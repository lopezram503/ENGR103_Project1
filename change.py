# Author: Ramiro Lopez
# GitHub username: lopezram503
# Date: 6/28/26
# Description: Asks the user for an amount in cents and
#              displays the fewest number of coins needed.

# Asks the user for an amount in cents.
print('Please enter an amount in cents less than a dollar.')

cents = int(input())

# Use floor division (//) and the mod operator (%) to calculate
# the number of quarters, dimes, nickles, and pennies.
quarters = cents // 25
remainder = cents % 25

dimes = remainder // 10
remainder = remainder % 10

nickles = remainder // 5
remainder = remainder % 5

pennies = remainder

# Displays the number of each coin.
print('Your change will be:')
print('Q:', quarters)
print('D:', dimes)
print('N:', nickles)
print('P:', pennies)

