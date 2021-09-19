def main():
    x = int(input())
    w = input()

    out = 0
    r = 1
    for i in range(x):
        out += (ord(w[i]) - 96) * r
        out %= 1234567891
        r *= 31
        r %= 1234567891
    print(out)


if __name__ == "__main__":
    main()
