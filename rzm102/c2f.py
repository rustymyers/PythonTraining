#!/usr/local/bin/python

import sys
try:
    temp_str = sys.argv[1]
    c = float(temp_str)
    f = ((9 * c) / 5 ) + 32
    print "{0:.1f} C is {1:.1f} F".format(c,f)
except (ValueError,IndexError),e:
    print "Please input a numeral. {0}".format(e)
    quit()