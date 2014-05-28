#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- c2f_func.py
#--------------------------------------------------------------------------------------------------
# Program    : c2f_func.py
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
#           2014-05-28 <rzm102>   Initial Version
#
# Version    : 1.0
#--------------------------------------------------------------------------------------------------

def c2f(c):
    c = ((9 * temp_float) / 5) + 32
    return c

import sys

while True:
    temp_string = raw_input("Enter Celsius temp: (or q to quit): ")
    if temp_string.lower() == "q": # or temp_string.lower() == "":
        print "Goodbye."
        break
    elif temp_string.lower() == "":
        print "Enter Degrees in Fahrenheit."
        continue
    else:
        temp_float = float(temp_string) 
        print "%.1f C is %.1f F" % (temp_float,c2f(temp_float))
