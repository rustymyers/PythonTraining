#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- compute.py
#--------------------------------------------------------------------------------------------------
# Program    : compute.py
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

# fruit1 = open("fruit1.txt")
# fruit2 = open("fruit2.txt")
# 
# fruit1_set = set(fruit1)
# fruit2_set = set(fruit2)
# 
# intersections = fruit1_set.intersection(fruit2_set)
# 
# for lines in intersections:
#     (fruit) = lines[:-1]
#     print fruit    



fruit1 = set()
fruit2 = set()

with open("fruit1.txt","r") as F1:
    for f in F1:
        fruit1.add(f.strip().lower())

with open("fruit2.txt","r") as F2:
    for f in F2:
        fruit2.add(f.strip().lower())

common = fruit1 & fruit2

print "\n".join(common)
