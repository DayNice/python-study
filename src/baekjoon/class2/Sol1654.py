from sys import stdin


def main():
    k, n = map(int, input().split())
    nums = list(int(stdin.readline()) for _ in range(k))
    out = get_best_length(n, nums)
    print(out)


def get_best_length(n, nums):
    first = 1
    last = max(nums)
    while first <= last:
        middle = (first + last) // 2
        count = get_count(middle, nums)
        if count >= n:
            first = middle + 1
        else:
            last = middle - 1
    return first - 1


def get_count(r, nums):
    count = sum(x // r for x in nums)
    return count


if __name__ == "__main__":
    main()
