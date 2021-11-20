from sys import stdin
import heapq


def main():
    n = int(input())
    heap = []
    out = []
    for _ in range(n):
        x = int(stdin.readline())
        if x != 0:
            heapq.heappush(heap, -x)
        else:
            if len(heap) > 0:
                out.append(str(-heapq.heappop(heap)))
            else:
                out.append("0")
    print("\n".join(out))


if __name__ == "__main__":
    main()
