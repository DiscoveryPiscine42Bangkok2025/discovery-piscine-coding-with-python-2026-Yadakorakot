import sys

def main():
	num = len(sys.argv) - 1

	if (num == 0):
		print("none")
		return 
	for i in range (1, num+1):
		if ("ism" not in sys.argv[i]):
			print(sys.argv[i] + "ism")
		else:
			continue
main() 