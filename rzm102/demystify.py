#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- demystify.py
#--------------------------------------------------------------------------------------------------
# Program    : demystify.py
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

read_file = open("mystery","rb")
bytes_of_file = read_file.read()
read_file.close()

print bytes_of_file[::2]