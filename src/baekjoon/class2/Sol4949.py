from sys import stdin


def main():
    out = []
    while (r := stdin.readline().rstrip()) != ".":
        out.append(get_result(r))
    print("\n".join(out))


def get_result(line):
    queue = []
    balanced = True
    for lt in line:
        if lt == "(" or lt == "[":
            queue.append(lt)
        elif lt == ")":
            if queue and queue[-1] == "(":
                queue.pop()
            else:
                balanced = False
                break
        elif lt == "]":
            if queue and queue[-1] == "[":
                queue.pop()
            else:
                balanced = False
                break
    if queue:
        balanced = False
    return "yes" if balanced else "no"


if __name__ == "__main__":
    main()
