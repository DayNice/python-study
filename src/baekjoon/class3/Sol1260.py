from sys import stdin
from collections import deque


def main():
    n, m, v = map(int, input().split())
    adj_lists = [list() for _ in range(n + 1)]
    for _ in range(m):
        i, j = map(int, stdin.readline().split())
        adj_lists[i].append(j)
        adj_lists[j].append(i)
    for p in adj_lists:
        p.sort()
    print(" ".join(map(str, dfs(n, v, adj_lists))))
    print(" ".join(map(str, bfs(n, v, adj_lists))))


def dfs(n, v, adj_lists):
    nums = []
    visited = [False] * (n + 1)
    stack = list()
    stack.append(v)
    while stack:
        v = stack.pop()
        if visited[v]:
            continue
        nums.append(v)
        visited[v] = True
        stack.extend(reversed(adj_lists[v]))
    return nums


def bfs(n, v, adj_lists):
    nums = []
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        if visited[v]:
            continue
        nums.append(v)
        visited[v] = True
        queue.extend(adj_lists[v])
    return nums


if __name__ == "__main__":
    main()
