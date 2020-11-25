import sys

def main():
  # input
  num = []
  for i in sys.stdin:
    num.append(list(map, int(i).split()))

  # output
  for i, name in enumerate(num[:-1]):
    if num[i][0] > num[i][1]:
      num[i][0], num[i][1] = num[i][1], num[i][0]
    print(num[i][0], num[i][1])


if __name__ == "__main__":
    main()
