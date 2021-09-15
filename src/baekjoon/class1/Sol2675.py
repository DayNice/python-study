def main():
    t = int(input())
    out = list()
    for _ in range(t):
        r, s = input().split()
        r = int(r)
        for lt in s:
            out.append(lt * r)
        out.append("\n")
    print("".join(out))


if __name__ == "__main__":
    main()
