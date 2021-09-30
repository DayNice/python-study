from sys import stdin
from collections import deque


def main():
    n = int(input())

    queue = deque()
    for i in range(n):
        line = stdin.readline().rstrip()
        w, *args = line.split()

        if w == "push":
            queue.append(args[0])
        elif w == "pop":
            print(queue.popleft() if queue else -1)
        elif w == "size":
            print(len(queue))
        elif w == "empty":
            print(0 if queue else 1)
        elif w == "front":
            print(queue[0] if queue else -1)
        elif w == "back":
            print(queue[-1] if queue else -1)


if __name__ == "__main__":
    main()
