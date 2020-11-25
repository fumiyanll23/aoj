def main():
  # input
  W, H, x, y, r = map(int, input().split())

  # compute
  flag = False
  if 0<=x-r and x+r<=W:
    if 0<=y-r and y+r<=H:
      flag = True

  # output
  if flag:
    print('Yes')
  else:
    print('No')

if __name__ == "__main__":
    main()
