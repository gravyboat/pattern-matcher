#!/usr/bin/python

'''
Author - Forrest Alvarez
Date - 2013-10-30
'''

import sys
import re

def patternMatcher(inputList):

	newInputList = inputList
	comparedAgainst = []
	comparedFrom = []
	matchedList = []
	'''
	We set up our values here for the 'keys', we also check to make sure they
	are integers.
	'''
	startOfVals = newInputList[0] + 1
	try:
		int(startOfVals)
	except ValueError:
		print('Non-integer value found in first key')

	endOfVals = newInputList[startOfVals] + startofVals + 1
	
	try:
		int(endOfVals)
	except ValueError:
		print('Non-integer value found in second key')

	try:
		for i in newInputList[1:(startofVals)]:
			comparedAgainst.append(i.replace(',', '/'))
	except:
		print("List length is inaccurate compared to key value.")

	try:
		for i in newInputList[startOfVals + 1:endOfVals]:
			comparedFrom.append(i)
	except:
		print("List length is inaccurate compared to key value.")

	for i in comparedFrom:
		if 
	
	regex code that loops through the values from list one, and compares them against list two
	The above code needs some logic for the matching, where a value matched on the furthest left is better
	than a value matched on a star, need to think of elegant solution, maybe compare multiple matches?
	code that takes all those values and puts them together.
	return(matchedList)


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
		outputList = patternMatcher(inputList)
		for i in outputList:
			sys.stdout.write(i + "\n")
