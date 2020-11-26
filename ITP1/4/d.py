def main():
  # input
  n = int(input())
  a = list(map(int, input().split()))

  # output
  print(min(a), max(a), sum(a))


if __name__ == '__main__':
  main()
