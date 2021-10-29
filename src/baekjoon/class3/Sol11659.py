from sys import stdin


def main():
    n, m = map(int, input().split())
    cum_sum = [0]
    for x in map(int, input().split()):
        cum_sum.append(cum_sum[-1] + x)
    out = []
    for _ in range(m):
        i, j = map(int, stdin.readline().split())
        out.append(str(cum_sum[j] - cum_sum[i - 1]))
    print("\n".join(out))


if __name__ == "__main__":
    main()
