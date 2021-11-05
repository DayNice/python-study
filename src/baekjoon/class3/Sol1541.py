def main():
    # input example : 55-50+40
    word_blocks = input().split("-")
    total = get_sum(word_blocks[0])
    for i in range(1, len(word_blocks)):
        total -= get_sum(word_blocks[i])
    print(total)


def get_sum(wb):
    return sum(map(int, wb.split("+")))


if __name__ == "__main__":
    main()
