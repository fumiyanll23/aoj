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
    up = '#' * edge[i][1]
    inside = '#' + '.'*(edge[i][1]-2) + '#'
    print(up)
    for j in range(edge[i][0]-2):
      print(inside)
    print(up)
    print()


if __name__ == '__main__':
  main()
