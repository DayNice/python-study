def main():
    n = int(input())
    count = 0
    while n >= 5:
        # count how many times 5 is multiplied into n!
        # (multiples of 5) + (multiples of 25) + (multiples of 125) + ...
        n //= 5
        count += n
    print(count)


if __name__ == "__main__":
    main()
