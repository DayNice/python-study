def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    out = get_best_length(nums, m)
    print(out)


def get_best_length(nums, m):
    first = 0
    last = max(nums)
    while first <= last:
        middle = (first + last) // 2
        total = sum(x - middle for x in nums if x > middle)
        if total >= m:
            first = middle + 1
        else:
            last = middle - 1
    return first - 1


if __name__ == "__main__":
    main()
