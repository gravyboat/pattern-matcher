#!/usr/bin/python

import sys
import itertools

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


def patternMatch(path, patterns):
	'''
	A path and list of patterns is provided, the path is then stripped of
	odd characters and split, then compared against each pattern. If the
	pattern is equal to the path it is added to a list, once all patterns
	have been explored a list is returned.
	'''
	newPatterns = patterns
	newPath = path
	matchedPatterns = []

	strippedPath = newPath.strip("/").split("/")
	for pattern in newPatterns:
		matches = 0
		strippedPattern = pattern.strip(",").split(",")
		if len(strippedPattern) != len(strippedPath):
			continue
		for i, field in enumerate(strippedPattern):
			try:
				if field == '*':
					matches += 1
				elif field == strippedPath[i]:
					matches += 1
			except:
				continue
		if matches == len(strippedPath):
			matchedPatterns.append(pattern)
	return(matchedPatterns)


def bestMatch(path, matches):
	'''
	If there is a tie (that is, if two or more patterns with the same number
	of wildcards match a path), prefer the pattern whose leftmost wildcard
	appears in a field further to the right. If multiple patterns' leftmost
	wildcards appear in the same field position, apply this rule recursively
	to the remainder of the pattern.

	For example: given the patterns `*,*,c` and `*,b,*`, and the path
	`/a/b/c/`, the best-matching pattern would be `*,b,*`.
	'''
	currentVal = len(path)
	wildcardVal = 0
	newVal = 0
	totalStars = len(path)
	strippedPath = path.strip("/").split("/")
	for match in matches:
		wildcardValNew = 0
		currentStars = 0
		strippedMatch = match.strip(",").split(",")
		for i, field in reversed(list(enumerate(strippedMatch))):
			if field == strippedPath[i]:
				newVal = i
				currentStars -= 1
			elif field == '*':
				wildcardValNew + i
		if newVal < currentVal:
			bestMatch = match
			currentVal = newVal
			totalStars = currentStars
			wildcardVal = wildcardValNew			
		elif currentStars < totalStars:
			bestMatch = match
			currentVal = newVal
			totalStars = currentStars
			wildcardVal = wildcardValNew
		elif wildcardValNew > wildcardVal:
			bestMatch = match
			wildcardVal = wildcardValNew

	return(bestMatch.split())


def doIt(inputList):
	'''
	Our doIt function simply kicks everything off, allowing a user to pass
	their input list to this single function, as opposed to each function.
	Once running it simply runs through the entire program.
	'''
	output = []
	patterns, paths = listSplitter(inputList)
	for path in paths:
		print(path, patterns)
		matches = patternMatch(path, patterns)
		if not matches:
			output.append(["NO MATCH"])
		if len(matches) > 1:
			output.append(bestMatch(path, matches))
		elif len(matches) == 1:
			output.append(matches)
	fixedOutput = list(itertools.chain(*output))
	return(fixedOutput)


if __name__ == '__main__':
	if sys.stdin.isatty():
		print("No file provided, exiting")
	elif not sys.stdin.isatty():
		inputList = []
		for line in sys.stdin.readlines():
			inputList.append(line.strip())
		finalList = doIt(inputList)
	for i in finalList:
		sys.stdout.write(i + "\n")	