#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- altlines.py
#--------------------------------------------------------------------------------------------------
# Program    : altlines.py
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

import sys

read_file = open("alt.txt")
if read_file:
    lines_of_file = read_file.readlines()
    read_file.close()

# Set up files to write to
a_file = open("a.txt","w")
b_file = open("b.txt","w")

print("This file has {0} lines. Let's write them to new files...".format(len(lines_of_file)))

line_counter = 0
for lines in lines_of_file:
    # Returns Even lines
    if not (line_counter % 2):
        # print("This line number is even: {0}".format(line_counter))
        a_file.write(lines)
    else:
        # print("This line number is odd: {0}".format(line_counter))
        b_file.write(lines)
    line_counter += 1

a_file.close()
b_file.close()