def main():
    n = int(input())
    m = int(input())
    # initialize is_broken
    is_broken = [False for _ in range(10)]
    # update is_broken
    if m > 0:
        for x in map(int, input().split()):
            is_broken[x] = True
    # get count and print
    out = get_min_count(n, m, is_broken)
    print(out)


def get_min_count(n, m, is_broken):
    min_count = abs(n - 100)
    if m == 10:
        # no buttons available
        return min_count
    # brute force search
    for x in range(1_000_000):
        r = get_btn_count(x, is_broken)
        if r > 0:
            min_count = min(min_count, r + abs(n - x))
    return min_count


def get_btn_count(x, is_broken):
    # -1 indicates an inaccessible number
    if x == 0:
        return -1 if is_broken[0] else 1
    count = 0
    while x > 0:
        x, c = divmod(x, 10)
        if is_broken[c]:
            return -1
        count += 1
    return count


if __name__ == "__main__":
    main()
