from sys import stdin


def main():
    n = int(input())
    data = [stdin.readline() for _ in range(n)]
    data.sort(key=lambda x: tuple(map(int, x.split()[::-1])))
    print("".join(data))


if __name__ == "__main__":
    main()
