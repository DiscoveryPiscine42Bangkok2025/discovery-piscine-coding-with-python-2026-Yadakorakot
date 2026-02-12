import sys

num = len(sys.argv) - 1

if (num == 0):
	print("none")
else:
	print(f"parameters: {num}")
	for i in range(1, num+1):
		print(f"{sys.argv[i]}: {len(sys.argv[i])}")