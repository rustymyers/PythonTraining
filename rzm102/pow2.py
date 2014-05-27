#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- pow2
#--------------------------------------------------------------------------------------------------
# Program    : pow2
# To Complie : n/a
#
# Purpose    : Print out all powers of 2 from 2^0 through 2^31
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


for x in xrange(0,32):
    print "2^{0:.1f} power = {1:.3f}".format(x,(2**x))