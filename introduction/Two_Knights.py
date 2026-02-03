n = int(input())

for k in range(1, n+1):
    if k == 1:
        print(0)
    else:
        squared = k * k
        ans = ((squared*(squared-1))//2) - (((2*(k-1) - 1)**2) - 1)
        print(ans)
