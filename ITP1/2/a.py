def main():
  # input
  a, b = map(int, input().split())

  # output
  if a < b:
    print('a < b')
  elif a > b:
    print('a > b')
  else:
    print('a == b')


if __name__ == "__main__":
    main()
