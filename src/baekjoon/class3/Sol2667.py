from collections import deque


def main():
    n = int(input())
    data = [input() for _ in range(n)]  # n strings of length n
    nums = get_nums(n, data)
    nums.sort()
    print(len(nums))
    print("\n".join(map(str, nums)))


def get_nums(n, data):
    nums = []
    # points marked as "1" must be visited
    unvisited = [list(map(lambda r: r == "1", p)) for p in data]
    for i in range(n):
        for j in range(n):
            if unvisited[i][j]:
                x = get_count(n, data, unvisited, i, j)  # spread and get count
                nums.append(x)
    return nums


def get_count(n, data, unvisited, x, y):
    # used to determine neighbor
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # breadth-first search algorithm
    queue = deque()
    queue.append((x, y))
    unvisited[x][y] = False
    count = 0
    while queue:
        x, y = queue.popleft()
        count += 1
        for k in range(4):
            i, j = x + dx[k], y + dy[k]
            if 0 <= i < n and 0 <= j < n and unvisited[i][j]:
                unvisited[i][j] = False
                queue.append((i, j))
    return count


if __name__ == "__main__":
    main()
