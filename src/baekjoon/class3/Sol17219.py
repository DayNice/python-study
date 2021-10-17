from sys import stdin


def main():
    n, m = map(int, input().split())
    name_map = {}
    for _ in range(n):
        w, p = stdin.readline().rstrip().split()
        name_map[w] = p
    out = []
    for _ in range(m):
        w = stdin.readline().rstrip()
        out.append(name_map[w])
    print("\n".join(out))


if __name__ == "__main__":
    main()
