def main():
    n = int(input())
    print(get_num(n))


def get_num(n):
    nums = [1, 1, 3]
    for i in range(3, n + 1):
        nums.append((nums[i - 1] + nums[i - 2] * 2) % 10007)
    return nums[n]


if __name__ == "__main__":
    main()
