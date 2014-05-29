#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- guessing.py
#--------------------------------------------------------------------------------------------------
# Program    : guessing.py
# To Complie : n/a
#
# Purpose    : Computer guesses number 0 through max value
#
# Called By  :
# Calls      :
#
# Author     : Rusty Myers <rzm102@psu.edu>
# Based Upon :
#
# Note       : 
#
# Revisions  : 
#           2014-05-27 <rzm102>   Initial Version
#
# Version    : 1.0
#--------------------------------------------------------------------------------------------------

import sys
import random

lowest_guess = int(100)

# Find the lowest number of guesses so far
with open("guesses.txt","r+") as guess_file:
    for line in guess_file:
        if 'lowest_guess' in line:
            a_low_guess = line.split("=")[1:]   
            a_low_guess = int(a_low_guess[0])
            print "{0} --- {1}".format(a_low_guess,lowest_guess)
            if int(a_low_guess) < int(lowest_guess):
                print "Lowest guess is {0}".format(lowest_guess)
                loweset_guess = a_low_guess
            else:
                print "{1} is Not loweset guess: {0}".format(lowest_guess,a_low_guess)
                
# Open a file for writing
fo = open ("guesses.txt","a")

# Get User Info
user_initials = raw_input("Please enter your initials for tracking: ")

# make a counter for guesses
guess_count = 1

# make a random number 1-100
computer_random = random.randrange(1,100+1)

# Set max value to 26 if none specified on command line
max_val = 26 if (len(sys.argv) <= 1) else int(sys.argv[1])
min_val = 0



# Ask user for the max value, set max_val as default
if len(sys.argv) == 1:
    update_max = raw_input("Enter max value (default="+str(max_val)+"): ")
    max_val = max_val if update_max == "" else int(update_max)

fo.write("User {0} is trying their hand at running the guessing game!\n".format(user_initials.lower()))

while True:
    comp_guess = (max_val + min_val) / 2
    if comp_guess < computer_random:
        print "Computer Guess: {0} is less than random number: {1}".format(comp_guess,computer_random)
        fo.write("Guess number {0} is {1}. Too Low.\n".format(guess_count,comp_guess))
        min_val = comp_guess
        guess_count += 1
    elif comp_guess > computer_random:
        print "Computer Guess: {0} is greater than random number: {1}".format(comp_guess,computer_random)
        max_val = comp_guess
        fo.write("Guess number {0} is {1}. Too High.\n".format(guess_count,comp_guess))
        guess_count += 1
    elif comp_guess == computer_random:
        print "Computer Guess: {0} is equal to random number: {1}".format(comp_guess,computer_random)
        print "I got it right! Yay!", "Run me again to play another round."
        fo.write("Guess number {0} is {1}. Correct!\n".format(guess_count,comp_guess))
        break
    # guess_answer = raw_input("Is your number " + str(comp_guess) + "?" + "\nEnter y = yes, h = higher, l = lower: ")
fo.write("It took {0} guesses to get the correct answer {1}. Nice job computer!\nlowest_guess={0}\n\n".format(guess_count,computer_random))
# close file
fo.close()