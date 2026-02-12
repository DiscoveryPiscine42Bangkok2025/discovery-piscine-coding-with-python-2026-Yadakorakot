import sys

num = len(sys.argv) - 1

if (num != 1):
	print("none")
else:
	word = input("What was the parameter? ")
	if (word == sys.argv[1]):
		print("Good job!")
	else:
		print("Nope, sorry...")