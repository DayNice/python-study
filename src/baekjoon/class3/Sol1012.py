from sys import stdin
from collections import deque


def main():
    t = int(input())
    out = []
    for _ in range(t):
        m, n, k = map(int, stdin.readline().split())
        data = [[False] * n for _ in range(m)]
        for _ in range(k):
            x, y = map(int, stdin.readline().split())
            data[x][y] = True
        out.append(str(get_count(m, n, data)))
    print("\n".join(out))


def get_count(m, n, unvisited):
    count = 0
    for i in range(m):
        for j in range(n):
            if unvisited[i][j]:
                count += 1
                spread(m, n, unvisited, i, j)
    return count


def spread(m, n, unvisited, x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((x, y))
    unvisited[x][y] = False
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            i, j = x + dx[k], y + dy[k]
            if 0 <= i < m and 0 <= j < n and unvisited[i][j]:
                unvisited[i][j] = False
                queue.append((i, j))


if __name__ == "__main__":
    main()
