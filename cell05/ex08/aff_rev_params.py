import sys

num = len(sys.argv) - 1

if num < 3:
    print("none")   
else:
    while (num > 0):
        print(sys.argv[num])
        num -= 1
