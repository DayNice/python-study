def main():
    line = input().strip()
    if line:
        print(line.count(" ") + 1)
    else:
        print(0)


if __name__ == "__main__":
    main()
