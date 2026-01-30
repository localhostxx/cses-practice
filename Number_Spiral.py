tcs = int(input())
for _ in range(tcs):
    x, y = map(int, input().split())
    max_number = max(x,y)
    starting_number = (max_number - 1) ** 2
    if max_number%2 is 0:
        print(starting_number + x + max_number - y) 
    else:
        print(starting_number + max_number - x + y)
