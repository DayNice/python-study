def main():
    n = int(input())
    data = set(map(int, input().split()))
    m = int(input())
    out = ["1" if x in data else "0" for x in map(int, input().split())]
    print("\n".join(out))


if __name__ == "__main__":
    main()
