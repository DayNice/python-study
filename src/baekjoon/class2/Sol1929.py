def main():
    m, n = map(int, input().split())
    is_prime = get_is_prime(n)
    out = [str(x) for x in range(m, n + 1) if is_prime[x]]
    print("\n".join(out))


def get_is_prime(n):
    # 0 ~ n
    is_prime = [False] * (n + 1)
    if n >= 2:
        is_prime[2] = True
    for x in range(3, n + 1, 2):
        is_prime[x] = True
    for x in range(3, int(n ** 0.5) + 1, 2):
        if is_prime[x]:
            for y in range(x * x, n + 1, x * 2):
                is_prime[y] = False
    return is_prime


if __name__ == "__main__":
    main()
