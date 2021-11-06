from sys import stdin


def main():
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, stdin.readline().split())))
    nums = [0, 0, 0]
    set_nums(nums, data, n, 0, 0)
    print("\n".join(map(str, nums)))


def set_nums(nums, data, n, x, y):
    if n == 1 or check(data, n, x, y):
        i = data[x][y] + 1
        nums[i] += 1
        return
    n = n // 3
    for i in range(3):
        for j in range(3):
            set_nums(nums, data, n, x + i * n, y + j * n)


def check(data, n, x, y):
    ref = data[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if data[i][j] != ref:
                return False
    return True


if __name__ == "__main__":
    main()
