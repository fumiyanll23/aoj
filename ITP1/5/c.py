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
    for j in range(edge[i][0]):
      for k in range(edge[i][1]):
        if (j+k)%2 == 0:
          print('#', end='')
        else:
          print('.', end='')
        if k == edge[i][1]-1:
          print()
      if j == edge[i][0]-1:
          print()


if __name__ == '__main__':
  main()
