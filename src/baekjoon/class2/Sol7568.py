def main():
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    ranks = [1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if data[i][0] > data[j][0] and data[i][1] > data[j][1]:
                ranks[j] += 1
            elif data[i][0] < data[j][0] and data[i][1] < data[j][1]:
                ranks[i] += 1
    print(" ".join(map(str, ranks)))


if __name__ == "__main__":
    main()
