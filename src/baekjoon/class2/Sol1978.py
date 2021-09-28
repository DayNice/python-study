def main():
    n = int(input())
    is_prime = get_is_prime()

    count = 0
    for x in map(int, input().split()):
        if is_prime[x]:
            count += 1

    print(count)


def get_is_prime():
    # 0 ~ 1000
    is_prime = [False] * 1001
    is_prime[2] = True
    for i in range(3, len(is_prime), 2):
        is_prime[i] = True

    limit = int(len(is_prime) ** 0.5)
    for i in range(3, limit + 1, 2):
        if is_prime[i]:
            for j in range(i * 2, len(is_prime), i):
                is_prime[j] = False
    return is_prime


if __name__ == "__main__":
    main()
