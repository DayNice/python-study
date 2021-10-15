from sys import stdin


def main():
    n, m = map(int, input().split())
    data = ["foo"]
    name_map = {}
    for i in range(1, n + 1):
        w = stdin.readline().rstrip()
        data.append(w)
        name_map[w] = i
    out = []
    for _ in range(m):
        w = stdin.readline().rstrip()
        if w.isnumeric():
            out.append(data[int(w)])
        else:
            out.append(str(name_map[w]))
    print("\n".join(out))


if __name__ == "__main__":
    main()
