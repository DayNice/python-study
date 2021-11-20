from sys import stdin
from collections import deque


def main():
    n, m = map(int, input().split())
    adj_lists = [list() for _ in range(n)]
    for _ in range(m):
        i, j = map(int, stdin.readline().split())
        # convert and apply as zero-base
        adj_lists[i - 1].append(j - 1)
        adj_lists[j - 1].append(i - 1)
    print(get_num(n, adj_lists))


def get_num(n, adj_lists):
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            spread(adj_lists, visited, i)
    return count


def spread(adj_lists, visited, x):
    visited[x] = True
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        for i in adj_lists[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


if __name__ == "__main__":
    main()
