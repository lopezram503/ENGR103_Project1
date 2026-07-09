# GitHub username: lopezram503
# Date: 7/8/26
# Description: This code is a guessing game. It asks one player to enter
# a number then another player keeps guessing until they get it right.
# The code lets the player know if each guess is too high or too low
# and then tells how many guesses it took.

print('Enter the integer for the player to guess.') # This lines tells the first player to enter to
# enter the number to be guessed.

guess_number = int(input()) # This line saves the number that the first player entered.

print(' Enter your guess.') # This line tells the second player to enter their guess

num = int(input()) # This line asks the other player to make their first guess.

count = 1 # This line starts counting the guesses. The first guess counts as 1.

while num != guess_number: # This line keeps the game going until the other player guesses the correct number.

    if num > guess_number: # This line checks the number guessed is higher than the correct number.
        print('Too high - try again:') # This line tells the player the guess was too high.

    else: # This line means that the guess was lower than the correct number
        print('Too low - try again:') # This line tells the player the guess was too low

    num = int(input()) # This line asks the player to make another guess.
    count = count + 1 # This line keeps track of how many guesses have been made by adding 1 to the count.

if count == 1: # This line checks if the player guessed the number on the first try.
    print('You guessed it in 1 try.') # This line lets the player know
else: # This lines runs if it took more than once to guess.
    print('You guessed it in ' , count, 'tries.') # This tells the player how many tries it took.