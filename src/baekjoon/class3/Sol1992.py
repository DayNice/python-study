def main():
    n = int(input())  # multiple of 2
    data = [input() for _ in range(n)]  # strings of length n
    out = get_result(data, n, 0, 0)
    print(out)


def get_result(data, n, x, y):
    if check(data, n, x, y):
        ref = data[x][y]
        return ref
    out = ["("]
    n = n // 2
    for i in range(2):
        for j in range(2):
            out.append(get_result(data, n, x + i * n, y + j * n))
    out.append(")")
    return "".join(out)


def check(data, n, x, y):
    ref = data[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if data[i][j] != ref:
                return False
    return True


if __name__ == "__main__":
    main()
