from collections import deque


def main():
    t = int(input())
    out = []
    for _ in range(t):
        p = input()
        n = int(input())
        # initialize data
        temp = map(int, input().strip("[]").split(","))
        data = deque(next(temp) for _ in range(n))
        # execute command and save result
        out.append(execute(p, n, data))
    print("\n".join(out))


def execute(p, n, data):
    toggled = False
    for c in p:
        if c == "R":
            toggled = not toggled
        elif c == "D":
            if len(data) == 0:
                return "error"
            if toggled:
                data.pop()
            else:
                data.popleft()
    return "[" + ",".join(map(str, reversed(data) if toggled else iter(data))) + "]"


if __name__ == "__main__":
    main()
