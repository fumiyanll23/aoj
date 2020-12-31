# import numpy as np

def main():
    # input
    n = int(input())
    move = [list(map(int, input().split())) for _ in range(n)]

    # compute
    ans = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(3)] for _ in range(4)]
    print(ans)


if __name__ == '__main__':
    main()
