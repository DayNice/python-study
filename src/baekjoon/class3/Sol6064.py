def main():
    t = int(input())
    nums = []
    for _ in range(t):
        m, n, x, y = map(int, input().split())
        nums.append(get_count(m, n, x, y))
    out = "\n".join(map(str, nums))
    print(out)


def get_count(m, n, x, y):
    # m must be smaller than or equal to n
    if m > n:
        m, n = n, m
        x, y = y, x
    # convert x, y to zero-base
    x, y = x - 1, y - 1
    # initialize variables
    i = x  # check <x, i>
    count = x + 1  # <x, x> is the (x + 1)th element
    # brute force
    limit = m * n
    while i != y:
        if count > limit:
            # no such element
            return -1
        i = (i + m) % n
        count += m
    return count


if __name__ == "__main__":
    main()
