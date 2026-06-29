# Author: Ramiro Lopez
# GitHub username: lopezram503
# Date: 6/28/26
# Description: Asks the user for Celsius temperature and
#              prints the Fahrenheit temperature.

# Asks the user for Celsius temperature
print('Please enter a Celsius temperature.')

celsius = float(input())

# Uses the Celsius temperature to find Fahrenheit.
# F=(9/5)C+32
fahrenheit = (9/5) * celsius + 32

# Shows the Fahrenheit temperature to the user.
print('The equivalent Fahrenheit temperature is:')
print(fahrenheit)