# to run: cat problem13.data | py problem13.py

import sys

def main():
	count = 0
	lines = sys.stdin.readlines()
	for line in lines:
		count = count + int(line)

	print(str(count)[:10])

main()