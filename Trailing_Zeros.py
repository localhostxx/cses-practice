n = int(input())
mul = 5
ans = 0
while mul <= n:
   ans += (n // mul)
   mul *= 5
print(ans) 
