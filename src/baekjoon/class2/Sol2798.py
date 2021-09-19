from itertools import combinations


def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    out = get_max_sum(n, m, nums)
    print(out)


def get_max_sum(n, m, nums):
    out = -1
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                r = nums[i] + nums[j] + nums[k]
                if out < r <= m:
                    out = r
    return out


def get_max_sum_alt(n, m, nums):
    out = -1
    for i in combinations(nums, 3):
        if out < (r := sum(i)) <= m:
            out = r
    return out


if __name__ == "__main__":
    main()
