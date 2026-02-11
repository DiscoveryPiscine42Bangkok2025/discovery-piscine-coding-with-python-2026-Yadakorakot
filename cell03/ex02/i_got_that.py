def main():
    print("what you gotta say? :", end=" ")
    txt = input()

    while txt is not " ":
        print("I got that! Anything else? :", end=" ")
        text = input()

        if text == "STOP":
            break
main()