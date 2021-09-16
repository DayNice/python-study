def main():
    t = int(input())
    for _ in range(t):
        words = input().split("X")
        out = 0
        for w in words:
            if (n := len(w)) > 0:
                out += n * (n + 1) // 2
        print(out)


if __name__ == "__main__":
    main()
