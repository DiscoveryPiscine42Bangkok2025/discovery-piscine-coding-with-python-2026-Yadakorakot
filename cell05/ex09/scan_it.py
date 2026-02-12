import sys
import re

num= len(sys.argv) - 1

if (num != 2):
	print("none")
else:
	word = sys.argv[1]
	txt = sys.argv[2]
	matches = re.findall(word, txt)
	print(len(matches))