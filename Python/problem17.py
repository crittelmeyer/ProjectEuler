def main():
	max = 1000
	numbersToAdd = []
	for i in range(1, max + 1):
		numbersToAdd.append(len(convertNumToSpelledNum(i).replace("-", "").replace(" ", "")))
	
	print(sum(numbersToAdd))

def convertNumToSpelledNum(num):
	if len(str(num)) == 1:
		return convertSingleDigitToSpelledDigit(num)
	elif len(str(num)) == 2:
		return convertDoubleDigitToSpelledDigit(num)
	elif len(str(num)) == 3:
		return convertTripleDigitToSpelledDigit(num)
	elif len(str(num)) == 4:
		return convertQuadrupleDigitToSpelledDigit(num)

def convertSingleDigitToSpelledDigit(digit):
	if digit == 0:
		return ""
	elif digit == 1:
		return "one"
	elif digit == 2:
		return "two"
	elif digit == 3:
		return "three"
	elif digit == 4:
		return "four"
	elif digit == 5:
		return "five"
	elif digit == 6:
		return "six"
	elif digit == 7:
		return "seven"
	elif digit == 8:
		return "eight"
	elif digit == 9:
		return "nine"

def convertDoubleDigitToSpelledDigit(num):
	if num == 0:
		return ""
	elif len(str(num)) == 1:
		return convertSingleDigitToSpelledDigit(num)
	elif str(num)[0] == "0":
		return convertSingleDigitToSpelledDigit(int(str(num)[1]))
	elif str(num)[0] == "1":
		if num == 10:
			return "ten"
		elif num == 11:
			return "eleven"
		elif num == 12:
			return "twelve"
		elif num == 13:
			return "thirteen"
		elif num == 14:
			return "fourteen"
		elif num == 15:
			return "fifteen"
		elif num == 16:
			return "sixteen"
		elif num == 17:
			return "seventeen"
		elif num == 18:
			return "eighteen"
		elif num == 19:
			return "nineteen"
	elif str(num)[0] == "2":
		return "twenty-" + convertSingleDigitToSpelledDigit(int(str(num)[1]))
	elif str(num)[0] == "3":
		return "thirty-" + convertSingleDigitToSpelledDigit(int(str(num)[1]))
	elif str(num)[0] == "4":
		return "forty-" + convertSingleDigitToSpelledDigit(int(str(num)[1]))
	elif str(num)[0] == "5":
		return "fifty-" + convertSingleDigitToSpelledDigit(int(str(num)[1]))
	elif str(num)[0] == "6":
		return "sixty-" + convertSingleDigitToSpelledDigit(int(str(num)[1]))
	elif str(num)[0] == "7":
		return "seventy-" + convertSingleDigitToSpelledDigit(int(str(num)[1]))
	elif str(num)[0] == "8":
		return "eighty-" + convertSingleDigitToSpelledDigit(int(str(num)[1]))
	elif str(num)[0] == "9":
		return "ninety-" + convertSingleDigitToSpelledDigit(int(str(num)[1]))
		
def convertTripleDigitToSpelledDigit(num):
	if num == 0:
		returnVal = ""
	elif len(str(num)) == 2:
		returnVal = convertDoubleDigitToSpelledDigit(num)
	elif len(str(num)) == 1:
		returnVal = convertSingleDigitToSpelledDigit(num)
	else:
		returnVal = convertSingleDigitToSpelledDigit(int(str(num)[0])) + "-hundred"
		if int(str(num)[1:]) != 0:
			returnVal = returnVal + " and " + convertDoubleDigitToSpelledDigit(int(str(num)[1:]))
	
	return returnVal

def convertQuadrupleDigitToSpelledDigit(num):
	returnVal = convertSingleDigitToSpelledDigit(int(str(num)[0])) + "-thousand"
	if int(str(num)[1:]) != 0:
		returnVal = returnVal + " " + convertTripleDigitToSpelledDigit(int(str(num)[1:]))
	return returnVal

main()