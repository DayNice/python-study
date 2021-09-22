def main():
    n = int(input())
    num = 666
    count = 1
    while count < n:
        num += 1
        x = num
        while x > 100:
            if x % 1000 == 666:
                count += 1
                break
            x = x // 10
    print(num)


def main_alt():
    # faster
    n = int(input())
    nums = {666}
    digits = 0
    while len(nums) < n:
        digits += 1
        for i in range(10 ** (digits - 1)):
            nums.add(666 * 10 ** digits + i)
        for i in range(10 ** (digits - 1), 10 ** digits):
            r = 1
            for j in range(digits + 1):
                x = i // r
                y = i % r
                nums.add(x * 1000 * r + 666 * r + y)
                r *= 10
    print(sorted(nums)[n - 1])


if __name__ == "__main__":
    main()
