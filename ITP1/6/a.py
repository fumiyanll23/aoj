def main():
    # input
    n = int(input())
    a = list(map(int, input().split()))

    # compute
    a_reverse = list(reversed(a))
    ans = ''
    for i in range(n-1):
        ans += str(a_reverse[i]) + ' '
    ans += str(a_reverse[n-1])

    # output
    print(ans)


if __name__ == '__main__':
    main()
