def main():
    n, r, c = map(int, input().split())
    out = get_num(2 ** n, r, c)
    print(out)


def get_num(m, r, c):
    if m == 2:
        return 2 * r + c
    m = m // 2
    return m ** 2 * (2 * (r // m) + (c // m)) + get_num(m, r % m, c % m)


if __name__ == "__main__":
    main()
