import sys

def main():
	# parse file into array
	names = sys.stdin.read()
	namesArray = names.replace("\"", "").replace("\n", "").split(",")

	# init total score to 0
	currTotalScore = 0

	# sort names alphabetically
	namesArray.sort()
	
	for i in range(0, len(namesArray)):
		currAlphaValue = getAlphabeticalValue(namesArray[i])
		print("processing " + namesArray[i] + "... adding " + str(currAlphaValue * (i + 1)) + " to " + str(currTotalScore))
		currTotalScore = currTotalScore + (currAlphaValue * (i + 1))

	print(currTotalScore)

def getAlphabeticalValue(word):
	wordArray = []
	wordLength = len(word)
	nameCharacters = list(word)
	alphabeticalValue = 0

	for i in range(0, wordLength):
		currLetterValue = ord(nameCharacters[i]) - 64
		# print("adding " + str(currLetterValue) + " to " + str(alphabeticalValue))
		alphabeticalValue = alphabeticalValue + currLetterValue

	return alphabeticalValue


main()