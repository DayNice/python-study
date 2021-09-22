from sys import stdin


def main():
    n = int(input())
    # -1_000_000 ~ 1_000_000
    contains = [False] * 2_000_001
    for _ in range(n):
        contains[int(stdin.readline()) + 1_000_000] = True

    out = list()
    for i in range(len(contains)):
        if contains[i]:
            out.append(str(i - 1_000_000))
            if len(out) > 1000:
                # save memory
                print("\n".join(out))
                out.clear()
    print("\n".join(out))


if __name__ == "__main__":
    main()
