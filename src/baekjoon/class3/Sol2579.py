from sys import stdin


def main():
    n = int(input())
    data = [int(stdin.readline()) for _ in range(n)]
    print(get_max_gain(data, n))


def get_max_gain(data, n):
    if n == 1:
        return data[0]
    # nums[i][0] : walked, nums[i][1] : jumped
    nums = [(data[0], data[0]), (data[0] + data[1], data[1])]
    for i in range(2, n):
        nums.append((nums[i - 1][1] + data[i], max(nums[i - 2]) + data[i]))
    return max(nums[n - 1])


if __name__ == "__main__":
    main()
