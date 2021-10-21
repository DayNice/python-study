from sys import stdin
from collections import deque


def main():
    n = int(input())
    m = int(input())
    links = [list() for _ in range(n + 1)]
    for _ in range(m):
        i, j = map(int, stdin.readline().split())
        # zero-based
        links[i - 1].append(j - 1)
        links[j - 1].append(i - 1)
    print(get_count(links, n))


def get_count(links, n):
    count = 0
    visited = [False] * n
    visited[0] = True
    queue = deque()
    queue.append(0)
    while queue:
        i = queue.popleft()
        for j in links[i]:
            if not visited[j]:
                visited[j] = True
                count += 1
                queue.append(j)
    return count


if __name__ == "__main__":
    main()
