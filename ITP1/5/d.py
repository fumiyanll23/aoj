def main():
  # input
  n = int(input())

  # cmpute
  ans, i = [], 1
  while i+1 <= n:
    i += 1
    x = i
    if x%3==0 or x%10==3:
      ans.append(i)
    while x:
      x //= 10

  # output
  for i in range(len(ans)):
    print(f' {ans[i]}', end='')


if __name__ == '__main__':
  main()
