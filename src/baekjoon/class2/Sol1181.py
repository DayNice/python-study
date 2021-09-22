from sys import stdin


def main():
    n = int(input())
    words = sorted(set(stdin.readline().rstrip() for _ in range(n)))
    words.sort(key=len)
    print("\n".join(words))


if __name__ == "__main__":
    main()
