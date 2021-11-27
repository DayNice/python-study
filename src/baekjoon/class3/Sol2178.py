from collections import deque

INF = 100000


def main():
    n, m = map(int, input().split())
    data = [input() for _ in range(n)]  # n strings of length m
    dist_matrix = get_dist_matrix(n, m, data)
    print(dist_matrix[n - 1][m - 1])


def get_dist_matrix(n, m, data):
    # used to determine neighbor
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # initialize dist_matrix based on data
    dist_matrix = []
    for i in range(n):
        row = list(map(lambda r: -1 if r == "1" else INF, data[i]))
        dist_matrix.append(row)
    # breadth-first search algorithm
    queue = deque()
    queue.append((0, 0))
    dist_matrix[0][0] = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            i, j = x + dx[k], y + dy[k]
            if 0 <= i < n and 0 <= j < m and dist_matrix[i][j] == -1:
                dist_matrix[i][j] = dist_matrix[x][y] + 1
                queue.append((i, j))
    return dist_matrix


if __name__ == "__main__":
    main()
