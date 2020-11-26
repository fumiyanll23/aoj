def main():
  # input
  a, b = map(int, input().split())

  # compute
  d = a // b
  r = a % b
  f = a / b

  # output
  print(f'{d} {r} {f:.5f}')


if __name__ == '__main__':
  main()
