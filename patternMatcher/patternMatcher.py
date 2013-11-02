#!/usr/bin/python

'''
Author - Forrest Alvarez
Date - 2013-11-01

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

def listSplitter(inputList):

	'''
	The listSplitter function takes in a single list, then splits it into
	two separate unique lists based on the key values. These lists are our
	patterns, and our paths. It then returns both of these lists.
	'''
	
	newInputList = inputList
	patternsList = []
	pathsList = []

	try:
		startOfPaths = int(newInputList[0]) + 1
	except ValueError:
		print('Non-integer value found in first key')
		sys.exit()

	try:
		endOfPaths = int(newInputList[startOfPaths]) + int(newInputList[0]) + 1
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

	'''
	The patternMatch function takes our paths, and our patterns and strips
	out any sort of split characters. It then compares the split pattern
	against the split path. If those values match it increments a variable.
	Once it checks a pattern if the length matches the path, it adds that
	pattern to a list. If no matches are found after checking all patterns
	it adds a 'NO MATCHES' entry to the list.
	'''

	newPatternsList = patternsList
	newPathsList = pathsList
	matchedList = []

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

	if sys.stdin.isatty():
		print("No file provided, exiting")

	elif not sys.stdin.isatty():
		inputList = []
		for line in sys.stdin.readlines():
			inputList.append(line.strip())
	patternsList, pathsList = listSplitter(inputList)
	a = patternMatch(patternsList, pathsList)
	for i in a:
		sys.stdout.write(i + "\n")
