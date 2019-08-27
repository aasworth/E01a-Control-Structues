#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')     # Prints "Greetings!" to the terminal.
colors = ['red','orange','yellow','green','blue','violet','purple']     #Creates a string array of different color options
play_again = ''     # Assigns the variable "play_again" to an empty string
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'):       # Starts a while loop with the conditional statements to make sure that play again is not set to no, and not to n
    match_color = random.choice(colors)     # This sets the variable match_color to a random choice of colors out of the color array
    count = 0   # Sets the count to 0
    color = '' # Sets the color to an empty string to begin
    while (color != match_color):   # Creates another while loop that runs to check what color the user enters
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line, and asks the user for input
        color = color.lower().strip()   # This takes the user input and strips the empty spaces from the beginning and end, and puts it to all lowercase
        count += 1      # Increments the variable count
        if (color == match_color):      # An if-loop to check if the user input color matches the random color chosen in line 14
            print('Correct!')       # Prints Correct
        else:   # A complement to the If/Else loop
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))      #Prints to the terminal letting the user know he/she did not guess correctly, and how many times they have guessed
    print('\nYou guessed it in {0} tries!'.format(count))   # This prints to the user that they have guessed correctly, and how many guesses it took. It doesn't need to be in the If/Else statement because all other cases are check already
    if (count < best_count):        #This is an if statement to check if the current count is lower than the best count recorded
        print('This was your best guess so far!')       #if the previous line returns true, it prints to the user that it was their best count of guesses
        best_count = count      #Because it was the best guess count, it makes that guess count the best_count variable
    play_again = input("\nWould you like to play again? ").lower().strip()      #This asks the user if they would like to play again, and strips blank space off it and makes it all lowercase if needed.
print('Thanks for playing!')        #Prints out to the user that the game is over, only if they answer no that they would not like to play again.