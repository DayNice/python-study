from sys import stdin
import heapq


def main():
    n = int(input())
    heap = []
    out = []
    for _ in range(n):
        x = int(stdin.readline())
        if x > 0:
            heapq.heappush(heap, x)
        elif x == 0:
            if heap:
                out.append(str(heapq.heappop(heap)))
            else:
                out.append("0")
    print("\n".join(out))


if __name__ == "__main__":
    main()
