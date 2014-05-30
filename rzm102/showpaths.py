#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- showpaths.py
#--------------------------------------------------------------------------------------------------
# Program    : showpaths.py
# To Complie : n/a
#
# Purpose    : Show pathname separator, variable separator, and extension separator for OS 
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
#           2014-05-30 <rzm102>   Initial Version
#
# Version    : 1.0
#--------------------------------------------------------------------------------------------------

import os

print "Pathname separator: ",os.path.sep
print "PATH separator: ",os.pathsep
print "Extension separator: ",os.extsep