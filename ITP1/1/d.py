def main():
  # input
  S = int(input())

  # compute
  h = S // 3600
  m = (S-h*3600) // 60
  s = S % 60
  ans = str(h)+':'+str(m)+':'+str(s)

  # output
  print(ans)


if __name__ == "__main__":
    main()
