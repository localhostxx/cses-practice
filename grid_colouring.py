grid = []
n, m = (map(int, input().split()))
for _ in range(n):
    grid.append(list(input()))

char_set = set(['A', 'B', 'C', 'D'])

def change_def(cordinate):
    x, y = cordinate

    excluded_set = set()
    excluded_set.add(grid[x][y])

    if x-1 >= 0:
        excluded_set.add(grid[x-1][y])
    if y-1 >= 0:
        excluded_set.add(grid[x][y-1])

    return (char_set.difference(excluded_set))

for i in range(n):
    for j in range(m):
        grid[i][j], *_ = change_def((i, j))
        print(grid[i][j], end="")
    print()


