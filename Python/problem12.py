# NOTE: Found a discussion about the "get number of factors for n"
# problem here: http://stackoverflow.com/questions/2844703/algorithm-to-find-the-factors-of-a-given-number-shortest-method
# It recommended the algorithms used in getFactorsCount2() and getFactorsCount3() below
# 2 seems to be the fastest - almost twice as fast as 3. The original getFactorsCount() I wrote never finished. Or at least I didn't wait long enough...


import cProfile

def main():
	maxFactors = 500
	factorsCount = 0
	currentNumber = 0

	while factorsCount <= maxFactors:
		currentNumber = currentNumber + 1
		triangle = getTriangle(currentNumber)
		factorsCount = getFactorsCount2(triangle)
	
	print(str(triangle) + " " + str(factorsCount))

def getTriangle(num):
	return sum(list(range(num + 1)))

def getFactorsCount(num):
	factors = []

	for i in range(1, num + 1):
		if num % i == 0:
			factors.append(i)

	return len(factors)

def getFactorsCount2(num):
	divisorsCount = 1
	i = 2
	while i * i < num:
		if num % i == 0:
			divisorsCount = divisorsCount + 1

		i = i + 1

	divisorsCount = divisorsCount * 2
	if i * i == num:
		divisorsCount = divisorsCount + 1

	return divisorsCount

def getFactorsCount3(num):
	initialNum = num
	divisorsCount = 1
	i = 2
	while i * i <= initialNum:
		power = 0
		while num % i == 0:
			num = num / i
			power = power + 1

		divisorsCount = divisorsCount * (power + 1)

		i = i + 1

	if num > 1:
		divisorsCount = divisorsCount * 2

	return divisorsCount

cProfile.run('main()')