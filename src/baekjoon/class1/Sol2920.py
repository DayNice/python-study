def main():
    nums = list(map(int, input().split()))
    ref = nums[1] - nums[0]
    out = "ascending" if ref > 0 else "descending"
    for i in range(1, len(nums) - 1):
        if nums[i + 1] - nums[i] != ref:
            out = "mixed"
            break
    print(out)


if __name__ == "__main__":
    main()
