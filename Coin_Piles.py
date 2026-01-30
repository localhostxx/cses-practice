tcs = int(input())

for _ in range(tcs):
    l, r = map(int, input().split())
    if l == 0 and r == 0:
        print("YES")
    elif l == 0 or r == 0:
        print("NO")
    else:
        print("YES" if (l+r)%3 == 0 else "NO")
