from sys import stdin


def main():
    # 1 ~ 500_000, odd integer
    n = int(input())
    # -4000 ~ 4000 integer
    counts = [0] * 8001
    total = 0
    max_val = -4001
    min_val = 4001

    # get counts, total, max value, min value
    for _ in range(n):
        x = int(stdin.readline())
        counts[x + 4000] += 1
        total += x
        if x > max_val:
            max_val = x
        if x < min_val:
            min_val = x

    # get median
    median = 0
    sum_counts = 0
    target = (n + 1) // 2
    # get mode
    mode = 0
    max_count = 0
    unique = True
    for x in range(min_val, max_val + 1):
        i = x + 4000
        if sum_counts < target:
            sum_counts += counts[i]
            median = x

        if counts[i] > max_count:
            mode = x
            max_count = counts[i]
            unique = True
        elif counts[i] == max_count and unique:
            mode = x
            unique = False

    # average
    print(round(total / n))
    # median
    print(median)
    # mode
    print(mode)
    # range
    print(max_val - min_val)


if __name__ == "__main__":
    main()
