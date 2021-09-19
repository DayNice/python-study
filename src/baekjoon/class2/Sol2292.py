def main():
    n = int(input())
    out = 1
    while n > 1:
        n -= out * 6
        out += 1
    print(out)


if __name__ == "__main__":
    main()
