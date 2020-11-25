import sys

def main():
  # input
  num = []
  for i in sys.stdin:
    num.append(int(i))

  # output
  for i, number in enumerate(num[:-1]):
    print(f'Case {i+1}: {number}')


if __name__ == "__main__":
    main()
