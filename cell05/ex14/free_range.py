import sys

num = len(sys.argv) - 1

if num != 2:
    print("none")
    sys.exit()

x = int(sys.argv[1])
y = int(sys.argv[2])

arr = list(range(x, y + 1))

print(arr)