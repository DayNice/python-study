from sys import stdin


def main():
    # 0 ~ 20
    contains = [False] * 21
    m = int(input())
    out = []
    for _ in range(m):
        w, *args = stdin.readline().rstrip().split()
        if w == "add":
            x = int(args[0])
            contains[x] = True
        elif w == "remove":
            x = int(args[0])
            contains[x] = False
        elif w == "check":
            x = int(args[0])
            out.append("1" if contains[x] else "0")
            if len(out) > 1000:
                print("\n".join(out))
                out.clear()
        elif w == "toggle":
            x = int(args[0])
            contains[x] = not contains[x]
        elif w == "all":
            contains = [True] * 21
        elif w == "empty":
            contains = [False] * 21
    print("\n".join(out))


if __name__ == "__main__":
    main()
