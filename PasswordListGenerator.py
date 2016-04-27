#Rishabh Shah
#2016
#Program that creates a text file of all possible passwords

import itertools
from progressbar import ProgressBar

possibleChars = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
minLength = 1
maxLength = 16
fh = open("passwords.txt", "a")
blankLine = """
"""

for n in xrange((minLength), (maxLength+1)):
    for xs in (itertools.product(possibleChars, repeat=n)):
        fh.write("".join(xs))
        fh.write(blankLine)

    print "Done with %d characters" %n