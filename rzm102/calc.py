#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- calc.py
#--------------------------------------------------------------------------------------------------
# Program    : calc.py
# To Complie : n/a
#
# Purpose    : use functions to do math promlems passed into the CLI
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

import sys

def addition(val1,val2):
    return int(val1) + int(val2)

def subtraction(val1,val2):
    return int(val1) - int(val2)

def division(val1,val2):
    if val1 == "0" or val2 == "0":
        print("Nothing happens with a 0!")
        return
    return float(val1) / float(val2)

def multiplication(val1,val2):
    return float(val1) * float(val2)


while True:
    math_string = raw_input("Enter math promblem (or q to quit): ")
    if math_string.lower() == "q": # or temp_string.lower() == "":
        print "Goodbye."
        break
    elif math_string.lower() == "":
        print "Enter math promblem (or q to quit): "
        continue
    else:
        val1,oper,val2 = math_string.split()
        print("You entered {0} {1} {2}".format(val1,oper,val2))
        
        if oper == "+":
            print addition(val1,val2)
        if oper == "-":
            print subtraction(val1,val2)
        if oper == "/":
            print division(val1,val2)
        if oper == "*":
            print multiplication(val1,val2)
