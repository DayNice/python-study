def main():
    nums = set()
    for _ in range(10):
        nums.add(int(input()) % 42)
    print(len(nums))


if __name__ == "__main__":
    main()
