def main():
    t = int(input())
    out = ""
    for i in range(t):
        a, b = map(int, input().split())
        out += str(a + b) + "\n"
    print(out)


if __name__ == "__main__":
    main()
