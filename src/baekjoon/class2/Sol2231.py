def main():
    n = int(input())
    out = 0
    for i in range(max(0, n - len(str(n) * 9)), n):
        if get_digit_sum(i) == n:
            out = i
            break
    print(out)


def get_digit_sum(x):
    out = x
    while x > 0:
        x, r = divmod(x, 10)
        out += r
    return out


def get_digit_sum_alt(x):
    out = sum(map(int, str(x))) + x
    return out


if __name__ == "__main__":
    main()
