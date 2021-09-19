def main():
    while (x := input()) != "0":
        if x == x[::-1]:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()
