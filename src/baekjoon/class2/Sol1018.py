def main():
    n, m = map(int, input().split())
    colors = [list(input()) for _ in range(n)]

    out = 32
    for i in range(n - 7):
        for j in range(m - 7):
            r = get_num(colors, i, j)
            if r < out:
                out = r
    print(out)


def get_num(colors, x, y):
    count = 0
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if (i + j) % 2 == 0:
                if colors[i][j] == "W":
                    count += 1
            else:
                if colors[i][j] == "B":
                    count += 1
    return min(count, 64 - count)


if __name__ == "__main__":
    main()
