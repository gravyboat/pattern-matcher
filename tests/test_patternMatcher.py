#!/usr/bin/python

'''
Author - Forrest Alvarez
Date - 2013-11-01

The patternMatcher tests are used to check all functions within the
patternMatcher.py script.
'''

import unittest
import sys
import os

sys.path.append(os.path.join('..', 'patternMatcher'))

from patternMatcher import listSplitter
from patternMatcher import patternMatch

'''
The input lists for splitting.
'''

splitInSimple = [3, 'x,y', '1,2,3', 'bar,foo', 
                4, 'x/y', '1/2/3/', 'bar/baz', 'bar/foo']
splitInComplex = [3, 'a,*,*', 'x,*,1', 'x,*,2', 
                4, 'a/b/c', 'x/4/1/', '/y/abc/2', 'a/c/d/a' ]
wildcardMatchIn = [2, '*,*,c', '*,b,*', 1, '/a/b/c/']

'''
Input lists for splitting specificall designed to return errors
'''

splitInTooManyPaths = [2, 'x,y', '1,2,3', 
                        2, 'x/y', '1/2/3/', 'bar/baz', 'bar/foo']
splitInNotEnoughPaths = [2, 'x,y', '1,2,3', 3, 'x/y', '1/2/4/']
splitInTooManyPatterns = [1, 'x,y', '1,2,3', 2, 'x/y', '1/2/4/']
splitInnotEnoughPatterns = [3, 'x,y', '1,2,3', 2, 'x/y', '1/2/4/']


'''
Our output lists for the matching. Also used as input for pattern matching.
'''

splitOutPatternsSimple = ['x,y', '1,2,3', 'bar,foo']
splitOutPathsSimple = ['x/y', '1/2/3/', 'bar/baz', 'bar/foo']
splitOutPatternsComplex = ['a,*,*', 'x,*,1', 'x,*,2']
splitOutPathsComplex = ['a/b/c', 'x/4/1/', '/y/abc/2', 'a/c/d/a']
splitOutWildcardPatterns = ['*,*,c', '*,b,*']
splitOutWildcardPaths = ['/a/b/c/']


'''
What the output from patternMatch should look like.
'''

simpleMatchOut = ['x,y', '1,2,3', 'NO MATCH', 'bar,foo']
complexMatchOut = ['a,*,*', 'x,*,1', 'NO MATCH', 'NO MATCH']
wildcardMatchOut = ['*,b,*']


class patternMatchTestCase(unittest.TestCase):

    def setup(self):
        self.simpleMatch = simpleMatch
        self.complexMatch = complexMatch
        self.weirdMatch = weirdMatch
        self.largeMatch = largeMatch

    '''
    Tests our function that splits the lists to ensure it returns the proper
    output.
    '''

    def test_simpleSplit(self):
        a, b = listSplitter(splitInSimple)
        self.assertEqual(a, splitOutPatternsSimple)
        self.assertEqual(b, splitOutPathsSimple)

    '''
    Tests our listSplitter function when we don't have enough paths for the
    key.
    '''

    def test_tooManyPathsSplit(self):
        listSplitter(splitInTooManyPaths)
        self.assertRaises(StandardError)

    '''
    Tests our listSplitter function when we have too many paths for the key.
    '''

    def test_NotEnoughPathsSplit(self):
        listSplitter(splitInNotEnoughPaths)
        self.assertRaises(StandardError)

    '''
    Tests our listSplitter function when we don't have enough patterns for the
    key.
    '''

    def test_tooManyPatternsSplit(self):
        listSplitter(splitInTooManyPatterns)
        self.assertRaises(StandardError)

    '''
    Tests our listSplitter function when we have too many paths for the key.
    '''

    def test_NotEnoughPatternsSplit(self):
        listSplitter(splitInnotEnoughPatterns)
        self.assertRaises(StandardError)

    '''
    Tests against an example that contains only a few simple items.
    '''

    def test_simpleMatch(self):
        a = patternMatch(splitOutPatternsSimple, splitOutPathsSimple)
        self.assertEqual(a, simpleMatchOut)

    '''
    Tests against an example that has several complex matches.
    '''
    def test_complexMatch(self):
        a = patternMatch(splitOutPatternsComplex, splitOutPathsComplex)
        self.assertEqual(a, complexMatchOut)

    '''
    Tests against items where multiple wildcards exists, but one is better.
    '''
    def test_wildcardMatch(self):
        a = patternMatch(splitOutWildcardPatterns, splitOutWildcardPaths)
        self.assertEqual(a, wildcardMatchOut)


if __name__ == '__main__':
    unittest.main()