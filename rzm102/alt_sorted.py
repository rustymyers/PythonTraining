#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- alt_sorted.py
#--------------------------------------------------------------------------------------------------
# Program    : alt_sorted.py
# To Complie : n/a
#
# Purpose    : Sort alt.txt by letter, then in order for "a" & reverse for "b"
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

# Set up files to write to
a_file = open("a_sorted.txt","w")
b_file = open("b_sorted.txt","w")

a_list = []
b_list = []

with open("alt.txt","r+") as alt_txt:
    for line in alt_txt:
        if line[:1] == 'a':
            a_list.append(line)
        if line[:1] == 'b':
            b_list.append(line)
a_sorted = sorted(a_list)
b_sorted = sorted(b_list,reverse=True)
print "".join(a_sorted)
print "".join(b_sorted)

a_file.close()
b_file.close()