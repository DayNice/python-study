def main():
    w = input()
    idx_of = [-1] * 26
    for i in range(len(w)):
        x = ord(w[i]) - 97
        if idx_of[x] == -1:
            idx_of[x] = i
    print(" ".join(map(str, idx_of)))


if __name__ == "__main__":
    main()
