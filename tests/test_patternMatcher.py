#!/usr/bin/python

import unittest
import sys

sys.path.append(os.path.join('..', 'patternMatcher'))

from patternMatcher import patternMatcher

# Our input lists for the matching, currently blank.

simpleMatch = []
complexMatch = []
weirdMatch = []
largeMatch = []
wildcardMatch = []

# Our output lists for the matching, currently blank.

simpleMatchOut = []
complexMatchOut = []
weirdMatchOut = []
largeMatchOut = []
wildcardMatchOut = []

class patternMatchTestCase(unittest.TestCase):

    def setup(self):
        self.simpleMatch = simpleMatch
        self.complexMatch = complexMatch
        self.weirdMatch = weirdMatch
        self.largeMatch = largeMatch


    # Tests against an example that contains only a few simple items.
    def test_simpleMatch(self):
        patternMatcherInstance = patternMatcher()
        matchedData = matchValues(self.simpleMatch)
        self.assertEqual(matchedData, simpleMatchOut)

    # Tests against an example that has several complex matches.
    def test_complexMatch(self):
        patternMatcherInstance = patternMatcher()
        matchedData = matchValues(self.complexMatch)
        self.assertEqual(matchedData, complexMatchOut)


    # Tests against an example which contains oddball items.
    def test_weirdMatch(self):
        patternMatcherInstance = patternMatcher()
        matchedData = matchValues(self.weirdMatch)
        self.assertEqual(matchedData, weirdMatchOut)

    # Tests against an example that's simple a lot of data to crunch.
    def test_largMatch(self):
        patternMatcherInstance = patternMatcher()
        matchedData = matchValues(self.largeMatch)
        self.assertEqual(matchedData, largeMatchOut)

    # Tests against items where multiple wildcards exists, but one is better.
    def test_wildcardMatch(self):
        patternMatcherInstance = patternMatcher()
        matchedData = matchValues(self.wildcardMatch)
        self.assertEqual(matchedData, wildcardMatchOut)


if __name__ == '__main__':
    unittest.main()