def main():
    n = int(input())
    x_points = list(map(int, input().split()))
    groups = {}  # stores indices of a particular value
    for i, x in enumerate(x_points):
        if x not in groups:
            groups[x] = []
        groups[x].append(i)
    new_x_points = [-1] * n
    for new_x, x in enumerate(sorted(groups.keys())):
        for i in groups[x]:
            new_x_points[i] = new_x
    print(" ".join(map(str, new_x_points)))


def main_alt():
    n = int(input())
    x_points = list(map(int, input().split()))
    transfer = {}  # a dictionary from old to new
    for new_x, x in enumerate(sorted(set(x_points))):
        transfer[x] = new_x
    new_x_points = list(map(transfer.__getitem__, x_points))
    print(" ".join(map(str, new_x_points)))


if __name__ == "__main__":
    main()
