from collections import deque

INF = 10_000_000


def main():
    m, n = map(int, input().split())  # n by m
    # initialize times
    times = []
    for i in range(n):
        row = [init_time(c) for c in map(int, input().split())]
        times.append(row)
    # set times
    set_times(n, m, times)
    out = get_max_times(n, m, times)
    print(-1 if out == INF else out)


def init_time(c):
    # 1 : ripe tomato -> time 0
    # 0 : fresh tomato -> time INF
    # -1 : no tomato -> time -1
    if c == 1:
        return 0
    elif c == 0:
        return INF
    else:
        return -1


def set_times(n, m, times):
    # used to determine neighbor
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # initialize queue
    queue = deque()
    for i in range(n):
        for j in range(m):
            if times[i][j] == 0:
                queue.append((i, j))
    # breadth-first search
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            i, j = x + dx[k], y + dy[k]
            if 0 <= i < n and 0 <= j < m and times[i][j] == INF:
                times[i][j] = times[x][y] + 1
                queue.append((i, j))


def get_max_times(n, m, times):
    max_val = times[0][0]
    for i in range(n):
        for j in range(m):
            max_val = max(max_val, times[i][j])
    return max_val


if __name__ == "__main__":
    main()
