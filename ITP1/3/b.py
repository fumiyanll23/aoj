def main():
  i = 0
  while True:
    # input
    num = int(input())
    i += 1

    # output
    if num != 0:
      ans = 'Case ' + str(i) + ': ' + str(num)
      print(ans)
    else:
      exit()


if __name__ == "__main__":
    main()
