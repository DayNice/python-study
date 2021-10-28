def main():
    n = int(input())
    data = sorted(map(int, input().split()))
    time = 0
    total = sum((time := time + x) for x in data)
    print(total)


if __name__ == "__main__":
    main()
