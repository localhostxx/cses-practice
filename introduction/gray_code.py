ans = [0]
n = int(input())
    
powers_of_two = set()
for i in range(n):
    powers_of_two.add(2**i)
    
numbers_set =set()
for num in range(1, 2**n):
    numbers_set.add(num)
    
for _ in range(1, 2**16):
    for power_two in powers_of_two:
        gray_code = ans[-1] ^ power_two
        if gray_code in numbers_set:
            ans.append(gray_code)
            numbers_set.remove(gray_code)
            break

for num in ans:
    print(f"{num:0{n}b}")
