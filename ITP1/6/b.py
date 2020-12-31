def main():
    # input
    n = int(input())
    cards = list(str(input().split()) for _ in range(n))

    # compute
    cards_sort = list(sorted(cards))
    print(cards_sort)


if __name__ == '__main__':
    main()
