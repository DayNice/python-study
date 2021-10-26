def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        data = {}
        for _ in range(n):
            v, k = input().split()
            data[k] = data.get(k, 0) + 1
        print(get_num(data))


def get_num(data):
    x = 1
    for count in data.values():
        x *= count + 1
    return x - 1


if __name__ == "__main__":
    main()
