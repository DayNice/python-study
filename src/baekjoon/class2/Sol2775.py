def main():
    nums = [list(range(15))]
    for i in range(1, 15):
        r = 0
        nums.append(list((r := r + nums[i - 1][j]) for j in range(15)))

    t = int(input())
    for _ in range(t):
        k = int(input())
        n = int(input())
        print(nums[k][n])


if __name__ == "__main__":
    main()
