import math

upperLimit = 28124

def main():
	global upperLimit
	sumAmicible = 0
 
	for i in range(2, upperLimit):
		factorsi = sumOfFactors(i)
		if factorsi > i and factorsi <= upperLimit:
			factorsj = sumOfFactors(factorsi)
			if factorsj == i:
				sumAmicible = sumAmicible + i + factorsi

	print(sumAmicible)

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

main()