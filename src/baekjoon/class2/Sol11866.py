def main():
    n, k = map(int, input().split())
    nums = get_nums(n, k)
    print("<" + ", ".join(map(str, nums)) + ">")


def get_nums(n, k):
    nums = []
    data = list(range(1, n + 1))

    i = 0
    while data:
        i = (i + k - 1) % len(data)
        nums.append(data.pop(i))

    return nums


if __name__ == "__main__":
    main()
