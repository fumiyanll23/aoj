import numpy as np

def main():
    # input
    n, m = map(int, input().split())
    A = np.array([list(map(int, input().split())) for _ in range(n)])
    b = np.array([int(input()) for _ in range(m)])

    # compute
    c = np.dot(A, b)

    # output
    for i in range(n):
        print(c[i])


if __name__ == '__main__':
    main()
