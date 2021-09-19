def main():
    x, y, w, h = map(int, input().split())
    out = min(x, w - x, y, h - y)
    print(out)


if __name__ == "__main__":
    main()
