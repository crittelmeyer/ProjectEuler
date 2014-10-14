# NOTE: main() below is my first pass at solving this problem, but it is quite slow
# see main2() for a much faster solution which I found here: http://www.mathblog.dk/project-euler-21-sum-of-amicable-pairs/

properDivisorSums = {}
amicableNumbers = {}
upperLimit = 10000

def main():
	global upperLimit

	for i in range(1, upperLimit + 1):
		properDivisorSums[i] = sum(getProperDivisors(i))

	for o in range(1, upperLimit + 1):
		currentProperDivisorSum = properDivisorSums[o]
		
		if currentProperDivisorSum > 0 and len(properDivisorSums) >= currentProperDivisorSum:
			possibleAmicableNumber = properDivisorSums[currentProperDivisorSum]

			if possibleAmicableNumber == o and currentProperDivisorSum != possibleAmicableNumber:
				amicableNumbers[possibleAmicableNumber] = currentProperDivisorSum
		
	amicableNumberSum = 0

	# now we have our amicable number pairs
	# iterate through each item
	for key in sorted(amicableNumbers.keys()):
		# simply add the keys (or values) of the amicable pair dictionary to find the answer
		amicableNumberSum = amicableNumberSum + int(key)

	print(amicableNumberSum)

def getProperDivisors(n):

	returnList = []

	#return list of numbers less than n that divide evenly into n
	for currNum in range(1, n):
		if n % currNum == 0:
			returnList.append(currNum)

	return returnList

import math

def main2():
	global upperLimit
	sumAmicible = 0
 
	for i in range(2, upperLimit):
		factorsi = sumOfFactors(i)
		if factorsi > i and factorsi <= upperLimit:
			factorsj = sumOfFactors(factorsi)
			if factorsj == i:
				sumAmicible = sumAmicible + i + factorsi

	print(sumAmicible)

# At this point in my career, I don't think I would have come upon this solution, because the implications of a relationship
# between a number and its square root escape me. After analyzing the sumOfFactors() function, I *think* I understand what's going on there.
# If you take the square root of any number, then you've essentially found the midway point for the list of its factors.
# For instance, the list of factors for 220 is 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110, 220.
# The square root of 220 is between 14 and 15, which would fall smack dab in the middle of our list of factors above.
# The reason this is important is because you can now just find the sum of exactly 1/2 of these numbers
# (using the square root as an upper or lower limit), and the other 1/2 of the sums will end up being matched up to one
# of each of the first 1/2 of sums... For example, for 220, we only have to find the matching multiple for each of these:
# 1, 2, 3, 4, 5, 10, 11 since these are the numbers below the square root of 220 (14.xx)
# The multiples that match with these first 7 numbers are 220, 110, 55, 44, 22, 20 which is the second 1/2 of our factor list
# So anyways, yeah it makes sense to me now, but I'm not sure if I'll recognize the opportunity to use square root in a similar fashion next time the opportunity arises
def sumOfFactors(number):
	sqrtOfNumber = int(math.sqrt(number))
	sum = 1
	#If the number is a perfect square
	#Count the squareroot once in the sum of factors
	if number == sqrtOfNumber * sqrtOfNumber:
		sum = sum + sqrtOfNumber;
		sqrtOfNumber = sqrtOfNumber - 1

	for i in range(2, sqrtOfNumber):
		if number % i == 0:
			sum = sum + i + (number / i)

	return sum




# print("should be [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]: " + str(getProperDivisors(220)))
# print("should be [1, 2, 4, 71, 142]: " + str(getProperDivisors(284)))

# print("should be 284: " + str(sum(getProperDivisors(220))))
# print("should be 220: " + str(sum(getProperDivisors(284))))

# main()
main2()