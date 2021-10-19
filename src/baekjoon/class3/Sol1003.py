def main():
    t = int(input())
    nums = get_nums()
    out = []
    for _ in range(t):
        n = int(input())
        out.append(f"{nums[n][0]} {nums[n][1]}")
    print("\n".join(out))


def get_nums():
    nums = [(1, 0), (0, 1)]
    for i in range(2, 41):
        temp = tuple(sum(i) for i in zip(nums[i - 1], nums[i - 2]))
        nums.append(temp)
    return nums


if __name__ == "__main__":
    main()
