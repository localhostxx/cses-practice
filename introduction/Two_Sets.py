n = int(input())
n_sum = n * (n+1) / 2

if n_sum % 2 == 0:
    print("YES")
    first_half , second_half = [], []
    half_sum = n_sum // 2
    
    for num in range(n, 0, -1):
        half_sum -= num
        if half_sum < 0 and half_sum != num:
            second_half.append(num)
            half_sum += num
        else:
            first_half.append(num)
    print(len(first_half))
    print(*first_half)
    print(len(second_half))
    print(*second_half)

else:
    print("NO")
