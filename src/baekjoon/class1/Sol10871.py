def main():
    n, x = map(int, input().split())
    out = ""
    for i in map(int, input().split()):
        if i < x:
            out += str(i) + " "
    print(out)


if __name__ == "__main__":
    main()
