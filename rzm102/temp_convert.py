#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- temp_convert.py
#--------------------------------------------------------------------------------------------------
# Program    : temp_convert.py
# To Complie : n/a
#
# Purpose    : Use TempConv module to do temp conversions
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
#           2014-05-29 <rzm102>   Initial Version
#
# Version    : 1.0
#--------------------------------------------------------------------------------------------------

import TempConv.convert as tc

def pp(*e):
    print "You Must Enter A Number!"
    pass


while True:
    conversion_type = raw_input("Ender F or C to do a temp conversion (or q to quit): ").lower()
    if conversion_type == "q":
        print "Run me again to convert the temps!"
        quit(0)
    if conversion_type == "c":
        temp_string = raw_input("Enter Celsius temp: (or q to quit): ")
        try:
            temp_float = float(temp_string)
        except (ValueError), e:
            pp(e)
            continue
        celcius = tc.c2f(temp_float)
        print "%.1f C is %.1f F" % (temp_float, celcius)
    elif conversion_type == "f":
        temp_string = raw_input("Enter Fahrenheit temp: (or q to quit): ")
        try:
            temp_float = float(temp_string)
        except (ValueError), e:
            pp(e)
            continue

        fahr = tc.f2c(temp_float)
        print "%.1f F is %.1f C" % (temp_float, fahr)
        