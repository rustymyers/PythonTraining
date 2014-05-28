#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- setsieve.py
#--------------------------------------------------------------------------------------------------
# Program    : setsieve.py
# To Complie : n/a
#
# Purpose    : use a set rather than a list to keep track of which numbers are non-prime
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

limit = 101
if len(sys.argv) > 1:
    limit = int(sys.argv[1]) + 1

flags = [True] * limit

for num in xrange(2,limit):
    if flags[num]:
        print num,
        for multiple_of_num in xrange(2*num,limit,num):
            flags[multiple_of_num] = False
