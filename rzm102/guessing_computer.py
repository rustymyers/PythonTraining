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

computer_random = random.randrange(1,100+1)

# Set max value to 26 if none specified on command line
max_val = 26 if (len(sys.argv) <= 1) else int(sys.argv[1])
min_val = 0

# Ask user for the max value, set max_val as default
if len(sys.argv) == 1:
    update_max = raw_input("Enter max value (default="+str(max_val)+"): ")
    max_val = max_val if update_max == "" else int(update_max)

while True:
    comp_guess = (max_val + min_val) / 2
    if comp_guess < computer_random:
        print "Computer Guess: {0} is less than random number: {1}".format(comp_guess,computer_random)
        min_val = comp_guess
    elif comp_guess > computer_random:
        print "Computer Guess: {0} is greater than random number: {1}".format(comp_guess,computer_random)
        max_val = comp_guess
    elif comp_guess == computer_random:
        print "Computer Guess: {0} is equal to random number: {1}".format(comp_guess,computer_random)
        print "I got it right! Yay!", "Run me again to play another round."
        break
    # guess_answer = raw_input("Is your number " + str(comp_guess) + "?" + "\nEnter y = yes, h = higher, l = lower: ")