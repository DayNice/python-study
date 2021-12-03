from sys import stdin
import heapq


def main():
    n = int(input())
    heap = []
    out = []
    for _ in range(n):
        x = int(stdin.readline())
        if x != 0:
            heapq.heappush(heap, (abs(x), x))
        else:
            if heap:
                out.append(heapq.heappop(heap)[1])
            else:
                out.append(0)
    print("\n".join(map(str, out)))


if __name__ == "__main__":
    main()
