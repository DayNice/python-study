def main():
    t = int(input())
    nums = get_nums()
    out = []
    for _ in range(t):
        n = int(input())
        out.append(str(nums[n]))
    print("\n".join(out))


def get_nums():
    nums = [1, 1, 2, 4]
    for i in range(4, 11):
        nums.append(nums[i - 1] + nums[i - 2] + nums[i - 3])
    return nums


if __name__ == "__main__":
    main()
