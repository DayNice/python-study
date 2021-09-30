from sys import stdin


def main():
    n = int(input())

    stack = []
    for i in range(n):
        line = stdin.readline().rstrip()
        w, *args = line.split()

        if w == "push":
            stack.append(args[0])
        elif w == "pop":
            print(stack.pop() if stack else -1)
        elif w == "size":
            print(len(stack))
        elif w == "empty":
            print(0 if stack else 1)
        elif w == "top":
            print(stack[-1] if stack else -1)


if __name__ == "__main__":
    main()
