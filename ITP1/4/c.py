def main():
  # input
  num, i = [], 0
  while True:
    num.append(list(map(str, input().split())))
    if num[i][1] == '?':
      break
    i += 1

  # output
  for i in range(len(num)-1):
    a, op, b = int(num[i][0]), num[i][1], int(num[i][2])
    if op == '+':
      print(a + b)
    elif op == '-':
      print(a - b)
    elif op == '*':
      print(a * b)
    else:
      print(a // b)


if __name__ == "__main__":
    main()
