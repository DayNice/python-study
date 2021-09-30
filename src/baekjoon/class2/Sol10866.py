from sys import stdin
from collections import deque


def main():
    n = int(input())

    my_deque = deque()
    for i in range(n):
        line = stdin.readline().rstrip()
        w, *args = line.split()

        if w == "push_front":
            my_deque.appendleft(args[0])
        elif w == "push_back":
            my_deque.append(args[0])
        elif w == "pop_front":
            print(my_deque.popleft() if my_deque else -1)
        elif w == "pop_back":
            print(my_deque.pop() if my_deque else -1)
        elif w == "size":
            print(len(my_deque))
        elif w == "empty":
            print(0 if my_deque else 1)
        elif w == "front":
            print(my_deque[0] if my_deque else -1)
        elif w == "back":
            print(my_deque[-1] if my_deque else -1)


if __name__ == "__main__":
    main()
