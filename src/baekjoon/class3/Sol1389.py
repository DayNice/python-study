from sys import stdin

INF = 10000


def main():
    n, m = map(int, input().split())
    dist_matrix = [[INF] * n for _ in range(n)]
    # distance to self is zero
    for i in range(n):
        dist_matrix[i][i] = 0
    for _ in range(m):
        i, j = map(int, stdin.readline().split())
        # convert to zero-base
        i -= 1
        j -= 1
        dist_matrix[i][j] = dist_matrix[j][i] = 1
    set_dist_matrix(n, dist_matrix)
    nums = get_row_sums(dist_matrix)
    # convert to one-base
    print(arg_min(nums) + 1)


def set_dist_matrix(n, dist_matrix):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])


def get_row_sums(dist_matrix):
    return list(sum(p) for p in dist_matrix)


def arg_min(nums):
    if len(nums) == 0:
        return -1
    i = 0
    for j in range(1, len(nums)):
        if nums[j] < nums[i]:
            i = j
    return i


if __name__ == "__main__":
    main()
