def main():
    n, k = map(int, input().split())
    out = get_num(n, k)
    print(out)


def get_num(n, k):
    nums = [list() for _ in range(n + 1)]
    for i in range(1, n + 1):
        nums[i].append(1)
        for j in range(1, i):
            nums[i].append(nums[i - 1][j - 1] + nums[i - 1][j])
        nums[i].append(1)
    return nums[n][k]


if __name__ == "__main__":
    main()
