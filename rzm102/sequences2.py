#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- sequences.py
#--------------------------------------------------------------------------------------------------
# Program    : sequences.py
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
#           2014-05-27 <rzm102>   Initial Version
#
# Version    : 1.0
#--------------------------------------------------------------------------------------------------

fruits = [
    '      MANGO', 'Apple', '      peach     ', 'PLUM     ', '   Apricot',
    'BaNaNa', 'Persimmon     '
]

clean_fruits = [ fruit.lower().strip() for fruit in fruits]
print ",".join(clean_fruits)

# Re-Order clean_fruits with new list
ordered_fruits = clean_fruits[1:]
ordered_fruits.append(clean_fruits[0])
print ",".join(ordered_fruits)

# Re-Order clean_fruits without new list
first_fruit = clean_fruits.pop(0)
clean_fruits.append(first_fruit)
print ",".join(clean_fruits)
