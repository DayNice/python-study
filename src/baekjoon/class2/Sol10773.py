from sys import stdin


def main():
    k = int(input())
    nums = []
    for i in range(k):
        x = int(stdin.readline())
        if x != 0:
            nums.append(x)
        else:
            nums.pop()
    print(sum(nums))


if __name__ == "__main__":
    main()
