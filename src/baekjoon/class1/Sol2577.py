def main():
    x = 1
    for _ in range(3):
        x *= int(input())
    x = str(x)
    for i in range(10):
        print(x.count(str(i)))


if __name__ == "__main__":
    main()
