def main():
    t = int(input())
    for _ in range(t):
        h, w, n = map(int, input().split())
        y = (n - 1) % h + 1
        x = (n - 1) // h + 1
        print(y * 100 + x)


if __name__ == "__main__":
    main()
