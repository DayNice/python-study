from sys import stdin


def main():
    n = int(input())
    data = [stdin.readline() for _ in range(n)]
    data.sort(key=lambda x: int(x.split()[0]))
    print("".join(data))


def main_alt():
    n = int(input())
    # 0 ~ 200
    blocks = [list() for _ in range(201)]
    for _ in range(n):
        line = stdin.readline()
        age = int(line.split()[0])
        blocks[age].append(line)
    print("".join("".join(b) for b in blocks))


if __name__ == "__main__":
    main()
