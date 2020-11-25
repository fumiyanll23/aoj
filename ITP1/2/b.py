def main():
  # input
  a, b, c = map(int, input().split())

  # output
  if a < b < c:
    print('Yes')
  else:
    print('No')


if __name__ == "__main__":
    main()
