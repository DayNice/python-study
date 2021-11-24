from collections import deque


def main():
    n, k = map(int, input().split())
    print(get_time(n, k))


def get_time(n, k):
    if n >= k:
        return n - k
    # initialize for 0 ~ 2 * k - 1
    times = [-1] * 2 * k
    # breadth-first search algorithm
    queue = deque()
    queue.append(n)
    times[n] = 0
    while queue:
        x = queue.popleft()
        if x == k:
            break
        for i in get_neighbors(k, x):
            if times[i] == -1:
                times[i] = times[x] + 1
                queue.append(i)
    return times[k]


def get_neighbors(k, x):
    neighbors = []
    if x < k:
        neighbors.append(x * 2)
        neighbors.append(x + 1)
    if x > 0:
        neighbors.append(x - 1)
    return neighbors


if __name__ == "__main__":
    main()
