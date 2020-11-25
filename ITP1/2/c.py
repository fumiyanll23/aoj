def main():
  # input
  num = list(map(int, input().split()))

  # compute
  num.sort()

  # output
  print(num[0], num[1], num[2])


if __name__ == "__main__":
    main()
