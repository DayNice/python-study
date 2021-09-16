def main():
    w = input().upper()
    unique = list(set(w))
    counts = get_counts(unique, w)
    out = get_argmax(counts)
    print(unique[out] if out != -1 else "?")


def get_counts(unique, w):
    map_lt = {lt: i for lt, i in zip(unique, range(len(unique)))}
    counts = [0] * len(unique)
    for lt in w:
        counts[map_lt[lt]] += 1
    return counts


def get_counts_alt(unique, w):
    # faster
    counts = []
    for lt in unique:
        counts.append(w.count(lt))
    return counts


def get_argmax(counts):
    max_val = -1
    out = -1
    for i in range(len(counts)):
        if counts[i] > max_val:
            max_val = counts[i]
            out = i
        elif counts[i] == max_val:
            out = -1
    return out


def get_argmax_alt(counts):
    # faster
    max_val = max(counts)
    out = counts.index(max_val) if counts.count(max_val) == 1 else -1
    return out


if __name__ == "__main__":
    main()
