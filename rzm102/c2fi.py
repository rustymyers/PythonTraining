#!/usr/local/bin/python

while True:
    try:
        temp_string = raw_input("Enter Celsius temp: (or q to quit): ")
        if temp_string.lower() == "q": # or temp_string.lower() == "":
            print "Goodbye."
            break
        elif temp_string.lower() == "":
            print "Enter Degrees in Fahrenheit."
            continue
        else:
            temp_float = float(temp_string)
            fahr = ((9 * temp_float) / 5) + 32
            print "%.1f C is %.1f F" % (temp_float,fahr)
    except  (ValueError,IndexError),e:
        print "Please input a numeral. {0}".format(e)
    