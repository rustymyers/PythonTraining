#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- guessing.py
#--------------------------------------------------------------------------------------------------
# Program    : guessing.py
# To Complie : n/a
#
# Purpose    : 
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

max_val = 26
min_val = 0

while True:
    comp_guess = (max_val + min_val) / 2
    guess_answer = raw_input("Is your number " + str(comp_guess) + "?" + "\nEnter y = yes, h = higher, l = lower: ")
    print 
    if guess_answer == "y":
        print "I got it right! Yay!"
        break
    elif guess_answer == "h":
        min_val = comp_guess
        continue
    elif guess_answer == "l":
        max_val = comp_guess
        continue