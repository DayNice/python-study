def main():
    n = int(input())
    out = -1
    for i in range(n % 5, n + 1, 5):
        if i % 3 == 0:
            out = (n - i) // 5 + i // 3
            break
    print(out)


if __name__ == "__main__":
    main()
