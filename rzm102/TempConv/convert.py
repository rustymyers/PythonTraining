#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- convert.py
#--------------------------------------------------------------------------------------------------
# Program    : convert.py
# To Complie : n/a
#
# Purpose    : module to convert F&C values
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

def c2f(c):
    "convert celcius to fahrenheit"
    return ((9 * float(c)) / 5 ) + 32
    
def f2c(c):
    "convert fahrenheit to celcius"
    return ((float(c) - 32 ) * 5 ) / 9

if __name__ == "__main__":
    print "Testing Code..."
    print "c2f -40: {0}".format(c2f(-40))
    print "c2f 0: {0}".format(c2f(0))
    print "c2f 100: {0}".format(c2f(100))
    print "f2c -40: {0}".format(f2c(-40))
    print "f2c 32: {0}".format(f2c(32))
    print "f2c 212: {0}".format(f2c(212))
    