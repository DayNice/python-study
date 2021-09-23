from sys import stdin


def main():
    n = int(input())
    # 0 ~ 10_000
    counts = [0] * 10_001
    for _ in range(n):
        counts[int(stdin.readline())] += 1

    for i in range(len(counts)):
        if counts[i] > 0:
            while counts[i] > 1000:
                print((str(i) + "\n") * 1000, end="")
                counts[i] -= 1000
            print((str(i) + "\n") * counts[i], end="")


if __name__ == "__main__":
    main()
