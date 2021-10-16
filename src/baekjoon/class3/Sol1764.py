from sys import stdin


def main():
    n, m = map(int, input().split())
    a = set(stdin.readline() for _ in range(n))
    b = set(stdin.readline() for _ in range(m))
    c = sorted(a & b)
    print(len(c))
    print("".join(c))


if __name__ == "__main__":
    main()
