def main():
    a, b, v = map(int, input().split())
    # ceil_((v - a) / (a - b)) + 1 = floor_((v - a - 1) / (a - b)) + 2
    out = (v - a - 1) // (a - b) + 2
    print(out)


if __name__ == "__main__":
    main()
