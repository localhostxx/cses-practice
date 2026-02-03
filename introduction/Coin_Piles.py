tcs = int(input())

for _ in range(tcs):
    l,r = map(int, input().split())
    min_rounds, flag = (l+r)//3, (l+r)%3 == 0
    
    if (l < min_rounds or r < min_rounds) or (not flag):
        print("NO")
    else:
        print("YES")
        
