def main():
    n = int(input())
    data = [input().split() for _ in range(n)]
    nums = [0, 0]
    set_nums(nums, data, n, 0, 0)
    print("\n".join(map(str, nums)))


def set_nums(nums, data, n, x, y):
    if check(data, n, x, y):
        i = int(data[x][y])
        nums[i] += 1
        return
    n = n // 2
    for i in range(2):
        for j in range(2):
            set_nums(nums, data, n, x + i * n, y + j * n)


def check(data, n, x, y):
    color = data[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if data[i][j] != color:
                return False
    return True


if __name__ == "__main__":
    main()
