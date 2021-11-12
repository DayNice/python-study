from sys import stdin


def main():
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(stdin.readline()))
    print(get_num(n, k, coins))


def get_num(n, k, coins):
    count = 0
    for i in range(n)[::-1]:
        if k == 0:
            break
        x, k = divmod(k, coins[i])
        count += x
    return count


if __name__ == "__main__":
    main()
