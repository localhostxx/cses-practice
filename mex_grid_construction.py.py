import heapq

n = int(input())
num_set = set(range(2*n))

ans = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    ans[0][i] = i
    ans[i][0] = i

def check_if_inside(cordinate):
    x,y = cordinate

    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    return True

def get_smallest_num(cordinate):
    x, y = cordinate
    excluded_set = set()

    for j in range(y):
        excluded_set.add(ans[x][j])

    for i in range(x):
        excluded_set.add(ans[i][y])
    diff_set = list(num_set.difference(excluded_set))
    heapq.heapify(diff_set)
    return diff_set[0]



for i in range(1, n):
    for j in range(1, n):
       ans[i][j] = get_smallest_num((i,j))

for row in ans:
    print(*row)
