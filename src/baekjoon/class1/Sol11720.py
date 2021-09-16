def main():
    n = int(input())
    w = input()
    out = 0
    for i in range(n):
        out += int(w[i])
    print(out)


if __name__ == "__main__":
    main()
