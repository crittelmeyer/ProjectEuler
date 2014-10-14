# first function below uses a helper function which slows down the process tremendously
# number 2 came more or less untouched from http://stackoverflow.com/questions/20768823/collatz-conjecture-sequence-length-using-a-python-generator
# 3 and 4 experimented with the differences between my original answer and 2
# seems the fastest are 2 and 4
# interesting to note is that the only difference between 3 and 4 is
# the order in which we check for odd/even - when we check for odd first
# it goes significantly faster. Perhaps there are more odd numbers than even in large Collatz sequences? So you only have to evaluate once...? not sure

import cProfile

def main():
	largestCollatzSum = 0
	startingNumberOfLargestCollatzSum = 1
	for startingNumber in range(1, 1000000):
		collatzSum = getCollatzSum4(startingNumber)
		if collatzSum > largestCollatzSum:
			largestCollatzSum = collatzSum
			startingNumberOfLargestCollatzSum = startingNumber

	print(startingNumberOfLargestCollatzSum)

def getCollatzSum(num):
	sum = 1
	while num != 1:
		num = doCollatzRule(num)
		sum = sum + 1

	return sum

def doCollatzRule(num):
	if num % 2 == 0:
		return num / 2

	return (3 * num) + 1

def getCollatzSum2(n):
	i = 1
	while n != 1:
		(n, i) = (3*n+1 if n%2 else n/2, i + 1)
    
	return i

def getCollatzSum3(num):
	sum = 1
	while num != 1:
		if num % 2 == 0:
			num = num / 2
		else:
			num = 3 * num + 1
		
		sum = sum + 1

	return sum

def getCollatzSum4(num):
	sum = 1
	while num != 1:
		if num % 2:
			num = 3 * num + 1
		else:
			num = num / 2
		
		sum = sum + 1

	return sum

cProfile.run('main()')