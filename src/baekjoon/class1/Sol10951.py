from sys import stdin


def main():
    out = ""
    for line in stdin.readlines():
        a, b = map(int, line.split())
        out += str(a + b) + "\n"
    print(out)


if __name__ == "__main__":
    main()
