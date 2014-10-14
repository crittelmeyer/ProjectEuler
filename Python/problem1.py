def main():
	maxNumber = 1000
	counter = 1
	multiples = []

	while counter < maxNumber:
		if isMultipleOfThree(counter):
			multiples.append(counter)
		elif isMultipleOfFive(counter):
			multiples.append(counter)

		counter = counter + 1

	print(sum(multiples))

def isMultipleOfThree(num):
	return num % 3 == 0

def isMultipleOfFive(num):
	return num % 5 == 0

main()