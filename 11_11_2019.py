def main():
    n = int(input("How many numbers buckeroo:"))
    x = n / 2
    if n%2 == 0:
        if x%2 == 0:
            print("2")
        else:
            print("1")
    else:
        print("0")


main()
