#!/usr/bin/python
"""
Solution to exercise 1 from lecture 1.
"""


def longest_seq(s, c):
    """
    Takes string s and character C as arguments and returns
    the length of the longest sequence of c-s in s.
    """
    longest = 0                         # length of the longest sequence so far
    where = 0                           # where we are in the string
    while True:
        where = s.find(c, where)        # find the next occurence of c
        if where == -1: break           # there is no c left in s
        length = 0                      # length of this sequence
        while s[where] == c:            # go through s until a different character is found
            where += 1
            length += 1
            if where == len(s): break   # stop at the end of s
        if length > longest: longest = length   # if this was the longest sequence so far, store its length
    print '\ninput string: {}'.format(s)
    print 'finding sequences of: {}'.format(c)
    print 'longest sequence: {}'.format(longest)


longest_seq('abbacccd','a')
longest_seq('abbacccd','b')
longest_seq('abbacccd','c')
longest_seq('abbacccd','f')
