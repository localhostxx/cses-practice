
def hanoi(n, l, m, r, ans):
    if n == 1:
        ans.append(f"{l} {r}")
    elif n == 2:
        ans.append(f"{l} {m}")
        ans.append(f"{l} {r}")
        ans.append(f"{m} {r}")
    else:
        hanoi(n-1, l, r, m, ans)
        ans.append(f"{l} {r}")
        hanoi(n-1, m, l, r, ans)

n = int(input())
ans = []
hanoi(n, 1, 2, 3, ans)
print(len(ans))
for step in ans:
    print(step)
