#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- countalice.py
#--------------------------------------------------------------------------------------------------
# Program    : countalice.py
# To Complie : n/a
#
# Purpose    : count number of lines in alice30.txt that contain Alice. (Should be 392).
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

open_file = open("alice30.txt","r")

line_counter = 0
for lines in open_file:
    if lines.find("Alice") >= 0:
        line_counter += 1
open_file.close()
print("Alice is found on {0} lines".format(line_counter))