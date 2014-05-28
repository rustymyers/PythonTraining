#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- chap8.py
#--------------------------------------------------------------------------------------------------
# Program    : chap8.py
# To Complie : n/a
#
# Purpose    : create function to clean up spam list
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

def cleanup(s):
    return s.strip().lower()

spam = [ 
    "Spam", 
    "eggs  ",
    "   spam    ",
    "     spam spam     ", 
    "SPAM	", 
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

for word in spam:
    print( "Before: >{0}< \nAfter:  >{1}<".format(word,cleanup(word))) 