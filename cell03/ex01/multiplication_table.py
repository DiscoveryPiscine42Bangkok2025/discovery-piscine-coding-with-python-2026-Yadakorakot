def main():
    print("Enter a number")
    num = int(input())
    keep = 0

    while num:
        result = num * keep

        print(keep, "x", num, "=", result)
        keep += 1

        if keep == num+2:
            break

main()