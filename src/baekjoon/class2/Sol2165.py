def main():
    n = int(input())
    nums = list(range(1, n + 1))

    # consider nums[i:] to be a valid queue
    # pop is accomplished by increasing i by 1
    # push is accomplished by appending elements to the end
    i = 1
    while i < len(nums):
        nums.append(nums[i])
        i += 2

    print(nums[-1])


def main_alt():
    n = int(input())
    nums = [0] * (n * 2)
    nums[:n] = range(1, n + 1)

    # consider nums[i:j] to be a valid queue
    # pop is accomplished by increasing i by 1
    # push is accomplished by setting nums[j] and increasing j by 1
    i = 1
    j = n
    while i < j:
        nums[j] = nums[i]
        j += 1
        i += 2

    print(nums[j - 1])


if __name__ == "__main__":
    main()
