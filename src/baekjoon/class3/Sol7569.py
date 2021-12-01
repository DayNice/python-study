from collections import deque

INF = 10_000_000


def main():
    m, n, h = map(int, input().split())  # h by n by m
    # initialize times and queue
    # 1 : ripe tomato -> time 0, add to queue
    # 0 : fresh tomato -> time INF
    # -1 : no tomato -> time -1
    times = []
    queue = deque()
    for i in range(h):
        temp = []
        for j in range(n):
            row = []
            for k, x in enumerate(map(int, input().split())):
                if x == 1:
                    row.append(0)
                    queue.append((i, j, k))
                elif x == 0:
                    row.append(INF)
                else:
                    row.append(-1)
            temp.append(row)
        times.append(temp)
    set_times(h, n, m, times, queue)
    out = get_max_time(h, n, m, times)
    print(-1 if out == INF else out)


def set_times(h, n, m, times, queue):
    # used to determine neighbors
    dx = [0, 0, 0, 0, 1, -1]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [1, -1, 0, 0, 0, 0]
    # breadth-first search
    while queue:
        x, y, z = queue.popleft()
        for r in range(6):
            i, j, k = x + dx[r], y + dy[r], z + dz[r]
            if 0 <= i < h and 0 <= j < n and 0 <= k < m and times[i][j][k] == INF:
                times[i][j][k] = times[x][y][z] + 1
                queue.append((i, j, k))
    return times


def get_max_time(h, n, m, times):
    max_val = times[0][0][0]
    for i in range(h):
        for j in range(n):
            for k in range(m):
                max_val = max(max_val, times[i][j][k])
    return max_val


if __name__ == "__main__":
    main()
