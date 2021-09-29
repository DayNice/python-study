def main():
    t = int(input())
    out = []
    for i in range(t):
        out.append(get_result(input()))
    print("\n".join(out))


def get_result(line):
    count = 0
    balanced = True
    for lt in line:
        if lt == "(":
            count += 1
        elif lt == ")":
            if count > 0:
                count -= 1
            else:
                balanced = False
                break
    if count > 0:
        balanced = False
    return "YES" if balanced else "NO"


if __name__ == "__main__":
    main()
