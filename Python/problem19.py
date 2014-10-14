weekDays = { 0: "Saturday",
				1: "Sunday",
				2: "Monday",
				3: "Tuesday",
				4: "Wednesday",
				5: "Thursday",	
				6: "Friday"
}

def main():
	global weekDays
	sundayCount = 0

	#loop through each month of each year from 1901 to 2000
	for currYear in range(1901, 2000 + 1):
		for currMonth in range(1, 12 + 1):
			currWeekDayOfFirstOfMonth = getWeekDayOfFirstOfMonth(currMonth, currYear)
			if currWeekDayOfFirstOfMonth == 1:
				sundayCount = sundayCount + 1
				# print(str(currMonth) + "/" + str(currYear) + ": " + weekDays[currWeekDayOfFirstOfMonth])

	print(str(sundayCount))

def getWeekDayOfFirstOfMonth(monthNumber, yearNumber):
	# print("checking month " + str(monthNumber))

	if yearNumber == 1950 and monthNumber == 1:
		return 1
	if yearNumber == 1900 and monthNumber == 1:
		return 2
	else:
		newMonthNumber = monthNumber - 1
		newYearNumber = yearNumber

		if monthNumber == 1:
			newMonthNumber = 12
			newYearNumber = newYearNumber - 1

		return getWeekDayOfOneMonthFrom(getWeekDayOfFirstOfMonth(newMonthNumber, newYearNumber), newMonthNumber, newYearNumber)

def getWeekDayOfOneMonthFrom(dayOfWeek, monthNumber, yearNumber):
	numberOfDaysInMonth = numberOfDays(monthNumber, yearNumber)

	return ((numberOfDaysInMonth % 7) + dayOfWeek) % 7

def numberOfDays(monthNumber, yearNumber):
	leapYear = isLeapYear(yearNumber)

	monthDays = { 1: 31,
					2: 29 if leapYear else 28,
					3: 31,
					4: 30,
					5: 31,
					6: 30,
					7: 31,
					8: 31,
					9: 30,
					10: 31,
					11: 30,
					12: 31
	}

	return monthDays[monthNumber]

def isLeapYear(yearNumber):

	#if year is divisible by 400, it's a leap year
	if yearNumber % 400 == 0:
		return True
	elif yearNumber % 4 == 0:

		#if year is divisible by 4 it's a leap year, unless it's also divisible by 100 (but not 400!)
		if yearNumber % 100 == 0:
			return False
		else:
			return True

	return False

# print("should be False: " + str(isLeapYear(1900)))
# print("should be True: " + str(isLeapYear(1904)))
# print("should be False: " + str(isLeapYear(1906)))
# print("should be False: " + str(isLeapYear(1907)))
# print("should be True: " + str(isLeapYear(1908)))
# print("should be True: " + str(isLeapYear(1996)))
# print("should be True: " + str(isLeapYear(2000)))

# print("should be 5: " + str(getWeekDayOfOneMonthFrom(2, 1, 1900)))
# print("should be 0: " + str(getWeekDayOfOneMonthFrom(4, 5, 1910)))
# print("should be 2: " + str(getWeekDayOfOneMonthFrom(6, 12, 1986)))
# print("should be 3: " + str(getWeekDayOfOneMonthFrom(7, 8, 2014)))

# print("should be 3: " + str(getWeekDayOfFirstOfMonth(6, 1937)))
# print("should be 0: " + str(getWeekDayOfFirstOfMonth(12, 1945)))
# print("should be 0: " + str(getWeekDayOfFirstOfMonth(7, 2000)))
# print("should be 1: " + str(getWeekDayOfFirstOfMonth(7, 2001)))


main()