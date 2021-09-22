def main():
    a, b = map(int, input().split())
    gcd = get_gcd(a, b)
    print(gcd, a * b // gcd, sep="\n")


def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


if __name__ == "__main__":
    main()
