import sys

num = len(sys.argv) - 1

if (num == 0 or ("z" not in sys.argv[1])):
	print("none")
else:
	if ("z" in sys.argv[1]):
		print("z"*sys.argv[1].count("z"))