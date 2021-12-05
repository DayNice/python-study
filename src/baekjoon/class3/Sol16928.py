from collections import deque


def main():
    n, m = map(int, input().split())
    # initialize portals as portals[i] = i
    portals = [i for i in range(101)]
    # set portals
    for _ in range(n + m):
        x, y = map(int, input().split())
        portals[x] = y
    # get count
    out = get_count(portals)
    print(out)


def get_count(portals):
    # initialize counts
    counts = [-1 for _ in range(101)]
    counts[1] = 0
    # initialize queue
    queue = deque()
    queue.append(1)
    # breadth-first search
    while queue:
        x = queue.popleft()
        if x == 100:
            break
        for k in range(1, 7):
            i = x + k
            if i > 100:
                continue
            i = portals[i]
            if counts[i] == -1:
                counts[i] = counts[x] + 1
                queue.append(i)
    return counts[100]


if __name__ == "__main__":
    main()
