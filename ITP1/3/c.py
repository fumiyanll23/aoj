import sys

def main():
  # input
  num, i = [], 0
  while True:
    num.append(list(map(int, input().split())))
    if num[i] == [0, 0]:
      break
    i += 1

  # output
  for i in range(len(num)-1):
    if num[i][0] > num[i][1]:
      num[i][0], num[i][1] = num[i][1], num[i][0]
    print(num[i][0], num[i][1])


if __name__ == "__main__":
    main()
