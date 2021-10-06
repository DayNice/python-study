def main():
    n, m, b = map(int, input().split())
    # 0 ~ 256
    counts = [0] * 257
    for _ in range(n):
        for x in map(int, input().split()):
            counts[x] += 1

    total_blocks = b + sum(x * counts[x] for x in range(257))
    max_level = total_blocks // (n * m)
    best_time, best_level = get_best_nums(counts, max_level)
    print(best_time, best_level)


def get_best_nums(counts, max_level):
    best_time = 500 * 500 * 256 * 2 + 1  # infinity
    best_level = -1
    for level in range(min(max_level, 256) + 1)[::-1]:
        time = get_time(counts, level)
        if time < best_time:
            best_time = time
            best_level = level
    return best_time, best_level


def get_time(counts, level):
    time = 0
    for i in range(level):
        time += (level - i) * counts[i]
    for i in range(level, 257):
        time += (i - level) * 2 * counts[i]
    return time


if __name__ == "__main__":
    main()
