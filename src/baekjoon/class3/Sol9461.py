def main():
    t = int(input())
    nums = get_nums()
    for _ in range(t):
        n = int(input())
        print(nums[n])


def get_nums():
    nums = [0, 1, 1, 1]
    for i in range(4, 101):
        nums.append(nums[i - 2] + nums[i - 3])
    return nums


if __name__ == "__main__":
    main()
