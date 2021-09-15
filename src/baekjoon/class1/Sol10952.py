def main():
    a, b = map(int, input().split())
    out = ""
    while (a, b) != (0, 0):
        out += str(a + b) + "\n"
        a, b = map(int, input().split())
    print(out)


if __name__ == "__main__":
    main()
