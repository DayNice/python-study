def main():
    n = int(input())
    nums = list(map(int, input().split()))
    max_val = max(nums)
    print(sum(nums) / n / max_val * 100)


if __name__ == "__main__":
    main()
