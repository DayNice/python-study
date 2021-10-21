def main():
    n = int(input())
    print(get_num(n))


def set_cache(func):
    cache = {}

    def wrapper(n):
        if n not in cache.keys():
            cache[n] = func(n)
        return cache[n]

    return wrapper


@set_cache
def get_num(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    return min(get_num(n // 3) + n % 3, get_num(n // 2) + n % 2) + 1


if __name__ == "__main__":
    main()
