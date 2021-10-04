from sys import stdin


def main():
    n = int(input())

    stack = []
    out = []
    count = 1
    for _ in range(n):
        x = int(stdin.readline())

        if count <= x:
            # push up to x
            for i in range(count, x + 1):
                stack.append(i)
                out.append("+")
            count = x + 1

        if stack[-1] == x:
            stack.pop()
            out.append("-")
        else:
            out.clear()
            out.append("NO")
            break

    print("\n".join(out))


if __name__ == "__main__":
    main()
