from collections import Counter


def main():
    n = int(input())
    # -10_000_000 ~ 10_000_000
    counts = [0] * 20_000_001
    for x in map(int, input().split()):
        counts[x + 10_000_000] += 1

    m = int(input())
    out = []
    for x in map(int, input().split()):
        out.append(str(counts[x + 10_000_000]))

    print(" ".join(out))


def main_alt():
    # memory efficient
    n = int(input())
    counts = Counter(map(int, input().split()))

    m = int(input())
    out = []
    for x in map(int, input().split()):
        out.append(str(counts[x]))

    print(" ".join(out))


if __name__ == "__main__":
    main_alt()
