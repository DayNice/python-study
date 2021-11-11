def main():
    n = int(input())
    m = int(input())
    data = input()
    print(get_num(n, m, data))


def get_num(n, m, data):
    ref = "IOI"
    num = 0
    count = 0
    i = 0
    while i < m - 2:
        if data[i:i + 3] == ref:
            count += 1
            i += 2
        else:
            count = 0
            i += 1
        if count >= n:
            num += 1
    return num


def get_num_alt(n, m, data):
    tokens = data.split("I")
    num = 0
    count = 0
    # trim both sides so that each token is surrounded by "I"
    for i in range(1, len(tokens) - 1):
        if len(tokens[i]) == 1:
            count += 1
        else:
            count = 0
        if count >= n:
            num += 1
    return num


if __name__ == "__main__":
    main()
