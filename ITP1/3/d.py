def main():
  # input
  a, b, c = map(int, input().split())

  # compute
  cnt = 0
  for i in range(a, b+1):
    if c%i == 0:
      cnt += 1

  # output
  print(cnt)


if __name__ == "__main__":
    main()
