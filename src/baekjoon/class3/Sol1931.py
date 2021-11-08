from sys import stdin
from operator import itemgetter


def main():
    n = int(input())
    data = []
    for _ in range(n):
        data.append(tuple(map(int, stdin.readline().split())))
    print(get_num(data))


def get_num(data):
    # activity selection problem
    # schedules that end faster have precedence
    # then sort by starting time to take into account cases where start == end
    data.sort(key=itemgetter(1, 0))
    time = 0
    count = 0
    for start, end in data:
        if time <= start:
            count += 1
            time = end
    return count


if __name__ == "__main__":
    main()
