import cProfile

def main():
	power = 1000

	bigValue = 2 ** power

	# print(int(sum_digits(bigValue)))
	# discovered a faster method for summing digits here: http://stackoverflow.com/questions/14939953/sum-the-digits-of-a-number-python
	# although for this challenge the above function worked just fine. very fast
	print(int(sum_digits_better(bigValue)))

def sum_digits(num):
  return sum( [ int(char) for char in str(num) ] )

def sum_digits_better(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

cProfile.run('main()')
# main()