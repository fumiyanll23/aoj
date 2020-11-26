def main():
  # input
  edge, i = [], 0
  while True:
    edge.append(list(map(int, input().split())))
    if edge[i][0]==0 and edge[i][1]==0:
      break
    i += 1

  # output
  N= len(edge)
  for i in range(N-1):
    ans = '#'*edge[i][1]
    for j in range(edge[i][0]):
      print(ans)
    print()


if __name__ == '__main__':
  main()
