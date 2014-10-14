import sys

def main():

	# loop through all rows
	lines = reversed(sys.stdin.readlines())
	previousLineArray = []
	currentLineArray = []
	i = 0
	for line in lines:
		if i == 0:

			#if we are on the first line, go ahead and set previous line array to first row
			previousLineArray = line.strip().split(" ")
		else:

			#if we are not on the first line, previous line array is already set and now we set the new current line array
			currentLineArray = line.strip().split(" ")

			#loop through all the numbers in this row
			for i in range(0, len(currentLineArray)):

				#compare the two descendent values and add the greater of the two to the current number
				if previousLineArray[i] >= previousLineArray[i + 1]:
					currentLineArray[i] = int(currentLineArray[i]) + int(previousLineArray[i])
				else:
					currentLineArray[i] = int(currentLineArray[i]) + int(previousLineArray[i + 1])

			#now we set the previous line array variable to our newly created current line array, making it ready for the next iteration through
			previousLineArray = currentLineArray

		#increase i by 1
		i = i + 1
	
	#print the answer
	print(str(currentLineArray))

main()