# Author: Ramiro Lopez
# GitHub username: lopezram503
# Date: 7/1/26
# Description: Using this code it will ask the user to enter how many integers
# they would like to enter, and then it reads each integer and determines the minimum
# and the maximum numbers.
#

num= int(input('How many integers would you like to enter?')) # This line
# asks how many integers you want to enter.

print(' Please enter', num, 'integers.') # This line tells the user to
# enter the integers.

number = int(input()) # This reads the first integer entered by the user.

max_num = number # This saves the first max number you enter
min_num = number # This saves the first min number you enter

for count in range(1,num): # This keeps asking the user for the rest of the integers.
    number = int(input()) # This reads the next integer entered by the user.

# This checks if the new number that was entered is larger than the current number
    if  number > max_num:
         max_num = number
# This checks if the new number that was entered is smaller than the current number
    if  number < min_num:
         min_num = number

print('min:', min_num) # This line will display your min number
print('max:', max_num) # This line will display your max number