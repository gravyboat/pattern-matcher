#!/usr/bin/python

'''
Author - Forrest Alvarez
Date - 2013-10-30

The patternMatcher script takes input that contains two key values, then a 
number of strings (such as 'x,y') equal to the value of the keys (for example,
if key one was equal to 5, there would be 5 strings following it). These 
sections are broken up into two lists and then compared against each other for
matches, it then returns a list based on the the matches it finds. If no match
is found then 'NO MATCH' is placed into the list. The pattern matcher has the
ability to match wildcard values as well.

The patternMatcher script uses stdin and stdout when referenced directly.
'''

import sys
import pdb

def listSplitter(inputList):
	
	newInputList = inputList
	patternsList = []
	pathsList = []

	'''
	We set up our values here for the 'keys', we also check to make sure they
	are integers.
	'''
	startOfPaths = int(newInputList[0]) + 1
	
	try:
		int(startOfPaths)
	except ValueError:
		print('Non-integer value found in first key')

	endOfPaths = int(newInputList[startOfPaths]) + int(newInputList[0]) + 1
	
	try:
		int(endOfPaths)
	except ValueError:
		print('Non-integer value found in second key')

	try:
		for i in newInputList[1:(startOfPaths)]:
			patternsList.append(i)
	except:
		print("List length is inaccurate compared to key value for patterns.")

	try:
		for i in newInputList[(startOfPaths + 1):(endOfPaths + 1)]:
			pathsList.append(i)
	except:
		print("List length is inaccurate compared to key value for paths.")

	return(patternsList, pathsList)

def patternMatch(patternsList, pathsList):

	newPatternsList = patternsList
	newPathsList = pathsList
	matchedList = []
	print(patternsList)
	print(pathsList)

	'''
	c = [3, 'x,y', '1,2,3', 'bar,foo', 4, 'x/y', '1/2/3/', 'bar/baz', 'bar/foo']
	'''

	for path in newPathsList:
		matchesFound = False
		strippedPath = path.strip("/").split("/")
		for pattern in newPatternsList:
			matches = 0
			strippedPattern = pattern.strip(",").split(",")
			for i, field in enumerate(strippedPattern):
				try:
					if field == '*':
						matches += 1
					elif field == strippedPath[i]:
						matches += 1
				except:
					continue
			
			if matches == len(strippedPath):
				matchedList.append(pattern)
				matchesFound = True
		if matchesFound == False:
			matchedList.append('NO MATCH')

	return(matchedList)
	

def bestMatch(pattern, allMatches):
	pass


if __name__ == '__main__':
	
	'''
	We check to see whether the input is a file, if it isn't we exit out.
	'''

	'''
	Our input file is taken, newlines are stripped, and it's run through the
	patternMatcher function, then the output is pushed back to stdout with
	newlines inserted since those would have been stripped out (and we want
	to return the data in the same format it was put into patternMatcher).
	'''

	#if sys.stdin.isatty():
	#	print("No file provided, exiting")

	#elif not sys.stdin.isatty():
	inputList = []
		#for line in sys.stdin.readlines():
		#	inputList.append(line.strip())
	c = [3, 'x,y', '1,2,3', 'bar,foo', 4, 'x/y', '1/2/3/', 'bar/baz', 'bar/foo']
	patternsList, pathsList = listSplitter(c)
	a = patternMatch(patternsList, pathsList)
	print(a)
