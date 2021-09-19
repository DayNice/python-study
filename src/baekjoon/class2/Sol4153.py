def main():
    nums = sorted(map(int, input().split()))
    while nums[2] != 0:
        if nums[0] ** 2 + nums[1] ** 2 == nums[2] ** 2:
            print("right")
        else:
            print("wrong")
        nums = sorted(map(int, input().split()))


if __name__ == "__main__":
    main()
