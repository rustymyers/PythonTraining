#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- c2floop.py
#--------------------------------------------------------------------------------------------------
# Program    : c2floop.py
# To Complie : n/a
#
# Purpose    : Prompt user for 
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


while True:
    temp_string = raw_input("Enter Celsius temp: (or q to quit): ")
    if temp_string.lower() == "q":
        print "Goodbye."
        break
    elif temp_string.lower() == "":
        print "Enter Degrees in Fahrenheit."
        continue
    else:
        temp_float = float(temp_string)
        fahr = ((9 * temp_float) / 5) + 32
        print "%.1f C is %.1f F" % (temp_float,fahr)


