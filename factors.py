# GitHub username: lopezram503
# Date: 7/6/26
# Description: Using this code will ask the user to enter a positive integer
# then checks each number from 1 up to the integer entered, and then it prints
# the numbers that factor into the users number.
#

num = int(input('Please enter a positive integer:'))  # This line asks the user for a positive number (integer)
# and it saves in (num).

print('The factors of', num, 'are:') # This line tells the user which number (num) we are going to find the factors of.

for number in range(1, num+1): # This line starts checking every number from 1 up to the number the user entered.
    if num % number == 0: # This line helps the users number be divided evenly if it can.
        print(number) # This prints the factor that was found.
