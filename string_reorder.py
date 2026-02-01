from collections import deque
unord_string = list(input())
unord_string.sort()

hash_table = [0 for _ in range(26)]
for char in unord_string:
    hash_table[ord(char) - 65] += 1

pq = deque()
for i in range(26):
    if hash_table[i]>0:
        pq.append(chr(65+i))

a, b = pq.popleft(), pq.popleft()
ans = ""
flag = True
impossible_flag = False

for _ in range(len(unord_string)):
    
    print(a, b, *pq)
    if flag:
        ans += a
        hash_table[ ord(a) - 65 ] -= 1
        flag = not flag

        if hash_table[ ord(a) - 65 ] == 0 and len(pq) > 0:
            # flag = not flag
            a = b
            b = pq.popleft()
    
    
    else:
        ans += b
        hash_table[ ord(b) - 65 ] -= 1
        flag = not flag
        
        if hash_table[ ord(b) - 65 ] == 0:
            if len(pq) == 0:
                b = pq.popleft()
    print(ans)

print(ans if not impossible_flag else "IMPOSSIBLE")
    
    
