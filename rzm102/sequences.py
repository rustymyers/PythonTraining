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

ctemps = [ -40.0, 0.0, 37.0, 75.0, 100.0 ]

Conversions = [ (ctemp,(((9 * ctemp) / 5) + 32)) for ctemp in ctemps]
# print Conversions
for ctemp,ftemp in Conversions:
    print "C = {0:.1f} ; F = {1:.1f}".format(ctemp,ftemp)