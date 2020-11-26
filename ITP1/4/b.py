from math import pi

def main():
  # input
  r = float(input())

  # compute
  area = pi * r**2
  length = 2 * pi * r

  # output
  print(f'{area:.5f} {length:.5f}')


if __name__ == '__main__':
  main()
