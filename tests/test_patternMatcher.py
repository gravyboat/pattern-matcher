#!/usr/bin/python

'''
Author - Forrest Alvarez
Date - 2013-10-30
'''

import unittest
import sys

sys.path.append(os.path.join('..', 'patternMatcher'))

from patternMatcher import patternMatcher

'''
Our input lists for the matching.
'''

simpleMatch = [3, 'x,y', '1,2,3', 'bar,foo', 
                4, 'x/y', '1/2/3/', 'bar/baz', 'bar/foo']
complexMatch = [3, 'a,*,*', 'x,*,1', 'x,*,2', 
                4, 'a/b/c', 'x/4/1/', '/y/abc/2', 'a/c/d/a' ]
weirdMatch = []
largeMatch = []
wildcardMatch = [2, '*,*,c', '*,b,*', 1, '/a/b/c/']

'''
Our output lists for the matching.
'''

simpleMatchOut = ['x,y', '1,2,3', 'NO MATCH', 'bar,foo']
complexMatchOut = ['a,*,*', 'x,*,1', 'NO MATCH', 'NO MATCH']
weirdMatchOut = []
largeMatchOut = []
wildcardMatchOut = ['*,b,*']

class patternMatchTestCase(unittest.TestCase):

    def setup(self):
        self.simpleMatch = simpleMatch
        self.complexMatch = complexMatch
        self.weirdMatch = weirdMatch
        self.largeMatch = largeMatch

    '''
    Tests against an example that contains only a few simple items.
    '''

    def test_simpleMatch(self):
        patternMatcherInstance = patternMatcher()
        matchedData = matchValues(self.simpleMatch)
        self.assertEqual(matchedData, simpleMatchOut)

    '''
    Tests against an example that has several complex matches.
    '''
    def test_complexMatch(self):
        patternMatcherInstance = patternMatcher()
        matchedData = matchValues(self.complexMatch)
        self.assertEqual(matchedData, complexMatchOut)

    '''
    Tests against an example which contains oddball items.
    NOT IMPLEMENTED
    '''
    def test_weirdMatch(self):
        patternMatcherInstance = patternMatcher()
        matchedData = matchValues(self.weirdMatch)
        self.assertEqual(matchedData, weirdMatchOut)

    '''
    Tests against an example that's simple a lot of data to crunch.
    NOT IMPLEMENTED
    '''
    def test_largMatch(self):
        patternMatcherInstance = patternMatcher()
        matchedData = matchValues(self.largeMatch)
        self.assertEqual(matchedData, largeMatchOut)

    '''
    Tests against items where multiple wildcards exists, but one is better.
    '''
    def test_wildcardMatch(self):
        patternMatcherInstance = patternMatcher()
        matchedData = matchValues(self.wildcardMatch)
        self.assertEqual(matchedData, wildcardMatchOut)


if __name__ == '__main__':
    unittest.main()