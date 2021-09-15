from sys import stdin


def main():
    nums = list(map(int, stdin.readlines()))
    i = max(range(len(nums)), key=nums.__getitem__)
    print(nums[i])
    print(i + 1)


if __name__ == "__main__":
    main()
