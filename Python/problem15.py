# note: while all versions of tryPath() below work, the first 4 are far too slow once you get past n = ~11.
# When n = 14, tryPath4() took ~35 seconds
# It's also important to note that this had already been tremendously refactored, as can be seen by the evolution from tryPath() to tryPath4() below
# After doodling/analyzing the problem on paper, I realized we were dealing with pascal triangles
# and that if I could find an algorithm to determine the nth row of a pascal triangle, then the largest number in that row would be the answer I am looking for
# getPascalValue() is the fruit of that realization

import cProfile

# validPaths = []
validPathsCount = 0
n = 20

def main():
	# tryPath('L')
	# tryPath('R')
	# print(len(validPaths))

	# Calculating amount of L + R was costing a lot...
	# tryPath2('L', 1, 0)
	# tryPath2('R', 0, 1)
	# print(len(validPaths))

	# Calculating length of path string was costing a lot...
	# tryPath3('L', 1, 1, 0)
	# tryPath3('R', 1, 0, 1)
	# print(len(validPaths))

	# Building a string at all was costing a lot...
	# tryPath4(1, 1, 0)
	# tryPath4(1, 0, 1)
	# print(validPathsCount)

	# realized you only needed to calculate half, then multiply by 2 at the end...
	# tryPath4(1, 1, 0)
	# print(validPathsCount * 2)

	# using the wikipedia page for Pascal's triangle, I created getPascalValue()
	# this function can quickly calculate a number from Pascals triangle, given the row number (n) and column number (k)
	# getPathLength() takes advantage of the similarity between Pascal's triangle and our grid paths problem

	# LATER:
	# The Pascal's triangle method turns out to not be the fastest way, according to projecteuler.net forum posts...
	# print(getPathLength(n))

def main2():
	# It's a combination problem. See http://betterexplained.com/articles/navigate-a-grid-using-combinations-and-permutations/
	# Also see http://betterexplained.com/articles/easy-permutations-and-combinations/
	
	# So now let's use combination method and see how much faster it is...
	print(factorial(2 * n) / (factorial(n) * factorial(n)))


	# RESULT:
	# In python, both results seem to be about the same speed
	# There may be more of a difference in results if ported to C/C++

def tryPath(pathString):
	if len(pathString) == n * 2:
		validPaths.append(pathString)
	else:
		if pathString.count("L") != n:
			tryPath(pathString + "L")

		if pathString.count("R") != n:
			tryPath(pathString + "R")

def tryPath2(pathString, lCount, rCount):
	if len(pathString) == n * 2:
		validPaths.append(pathString)
	else:
		if lCount != n:
			tryPath2(pathString + "L", lCount + 1, rCount)

		if rCount != n:
			tryPath2(pathString + "R", lCount, rCount + 1)

def tryPath3(pathString, pLen, lCount, rCount):
	if pLen == n * 2:
		validPaths.append(pathString)
	else:
		if lCount != n:
			tryPath3(pathString + "L", pLen + 1, lCount + 1, rCount)

		if rCount != n:
			tryPath3(pathString + "R", pLen + 1, lCount, rCount + 1)

def tryPath4(pLen, lCount, rCount):
	if pLen == n * 2:

		global validPathsCount
		validPathsCount = validPathsCount + 1
	else:
		if lCount != n:
			tryPath4(pLen + 1, lCount + 1, rCount)

		if rCount != n:
			tryPath4(pLen + 1, lCount, rCount + 1)

def getPathLength(n):
	return getPascalValue(n * 2, n)

def getPascalValue(n, k):
	if k == 0:
		return 1
	else:
		return getPascalValue(n, k - 1) * ((n + 1 - k) / k)

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

cProfile.run('main()')
# cProfile.run('main2()')
# main()