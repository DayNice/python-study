def main():
    n = int(input())
    # initialize adjacency matrix
    adj_matrix = []
    for _ in range(n):
        adj_matrix.append(list(map(int, input().split())))
    # set adjacency matrix
    set_adj_matrix(n, adj_matrix)
    # print adjacency matrix
    for p in adj_matrix:
        print(" ".join(map(str, p)))


def set_adj_matrix(n, adj_matrix):
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adj_matrix[i][j] != 1 and adj_matrix[i][k] == 1 and adj_matrix[k][j] == 1:
                    adj_matrix[i][j] = 1


if __name__ == "__main__":
    main()
