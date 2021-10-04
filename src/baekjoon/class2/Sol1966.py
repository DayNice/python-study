from collections import deque


def main():
    t = int(input())

    out = []
    for _ in range(t):
        n, m = map(int, input().split())

        data = deque()
        counts = [0] * 10
        for item in enumerate(map(int, input().split())):
            # (index, priority)
            data.append(item)
            counts[item[1]] += 1

        out.append(str(get_num(data, counts, m)))

    print("\n".join(out))


def get_num(data, counts, m):
    num = 0
    for i in range(len(counts))[::-1]:
        # repeat counts[i] times
        for _ in range(counts[i]):
            # while priority is not i
            while data[0][1] != i:
                data.rotate(-1)
            num += 1
            # pop and check
            if data.popleft()[0] == m:
                return num
    # fail check
    return -1


if __name__ == "__main__":
    main()
