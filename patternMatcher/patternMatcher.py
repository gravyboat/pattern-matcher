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
import re

def listSplitter(inputList):
	
	newInputList = inputList
	patternsList = []
	pathsList = []

	'''
	We set up our values here for the 'keys', we also check to make sure they
	are integers.
	'''
	startOfPatterns = newInputList[0] + 1
	try:
		int(startOfPatterns)
	except ValueError:
		print('Non-integer value found in first key')

	endOfPaths = newInputList[startOfPatterns] + startOfPatterns + 1

	try:
		int(startOfPaths)
	except ValueError:
		print('Non-integer value found in second key')

	try:
		for i in newInputList[1:(startOfPatterns)]:
			patternsList.append(i)
	except:
		print("List length is inaccurate compared to key value.")

	try:
		for i in newInputList[startOfPaths + 1:endofPaths]:
			pathsList.append(i)
	except:
		print("List length is inaccurate compared to key value.")

	return(patternsList, pathsList)

def patternMatcher(patternsList, pathsList):

	newPatternsList = patternsList
	newPathsList = pathsList
	matchedList = []

	for pattern in newPatternsList:
		strippedPattern = pattern.strip(",").split(",")
		for path in newPathsList:
			strippedPath = path.strip("/").split("/")
			if strippedPattern == strippedPath:
				matchedList.append(strippedPattern)





	for i in comparedFrom:
		if 
	
	regex code that loops through the values from list one, and compares them against list two
	The above code needs some logic for the matching, where a value matched on the furthest left is better
	than a value matched on a star, need to think of elegant solution, maybe compare multiple matches?
	code that takes all those values and puts them together.
	return(matchedList)

def bestMatch(pattern, allMatches):


if __name_ == '__main__':
	
	'''
	We check to see whether the input is a file, if it isn't we exit out.
	'''

	if sys.stdin.isatty():
		print("No file provided, exiting")

	'''
	Our input file is taken, newlines are stripped, and it's run through the
	patternMatcher function, then the output is pushed back to stdout with
	newlines inserted since those would have been stripped out (and we want
	to return the data in the same format it was put into patternMatcher).
	'''

	elif not sys.stdin.isatty():
		inputList = []
		for line in sys.stdin.readlines():
			inputList.append(line.strip())
		patternsList, pathsList = listSplitter(inputList)
		for i in outputList:
			sys.stdout.write(i + "\n")
