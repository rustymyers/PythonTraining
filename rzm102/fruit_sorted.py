#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- fruit_sorted.py
#--------------------------------------------------------------------------------------------------
# Program    : fruit_sorted.py
# To Complie : n/a
#
# Purpose    : Sort Fruit.txt by:
#                   name - case-sensitive
#                   name - case-insensitive
#                   length of name, then name
#                   sorted by 2nd letter, then first letter
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

fruit_list = []

with open("fruit.txt","r+") as fruit_text:
    for line in fruit_text:
        fruit_list.append(line)

# Case sensitive sort
fruit_sorted = sorted(fruit_list)

# Case insensitive sort
fruit_sorted_insense = sorted(fruit_list,key=lambda e: e.lower())

# length of name, then name
fruit_sorted_len_name = sorted(fruit_list,key=lambda e: (len(e),e.lower()))

# sort by 2nd letter, than first
fruit_sorted_2nd_1st = sorted(fruit_list,key=lambda e: (e[1:2].lower(),e[0:1].lower()))
print "Original Fruit List"
print "".join(fruit_list)
print "Fruit Sorted Case-sensitive"
print "".join(fruit_sorted)
print "Fruit Sorted Case-Insensitive"
print "".join(fruit_sorted_insense)
print "Fruit Sorted Length, Name"
print "".join(fruit_sorted_len_name)
print "Fruit Sorted char #2, char #1"
print "".join(fruit_sorted_2nd_1st)