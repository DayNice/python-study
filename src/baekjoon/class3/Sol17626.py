def main():
    n = int(input())
    a = set(i ** 2 for i in range(1, int(n ** 0.5) + 1))
    b = set(n - i - j for i in a for j in a)
    out = -1
    if n in a:
        out = 1
    elif 0 in b:
        out = 2
    elif len(a & b) != 0:
        out = 3
    else:
        out = 4
    print(out)


if __name__ == "__main__":
    main()
