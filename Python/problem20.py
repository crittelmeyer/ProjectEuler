n = 100

def main():
	global n

	factorialValue = factorial(n)
	print(sum_digits_better(factorialValue))
	#NOTE: used sum_digits_better() function from problem 16 to solve this

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n - 1)

def sum_digits_better(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

main()