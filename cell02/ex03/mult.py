
print("Enter your first number:")
fnum = int(input())
firstnum = str(fnum)

print("Enter your second number:")
snum = int(input())
secondnum = str(snum)

result = fnum * snum

if result > 0:
    print(firstnum, " x ", secondnum, " = ", result)
    print("The result is positive.")
elif result < 0:
    print(firstnum, " x ", secondnum, " = ", result)
    print("The result is negative.")
elif result == 0:
    print(firstnum, " x ", secondnum, " = ", result)
    print("The result is positive and negative.")

