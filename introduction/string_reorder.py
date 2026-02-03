input_str = input()
hash_map = [0]*26

for char in input_str:
    hash_map[ord(char) - 65] += 1

ans = ""

for _ in input_str:
    char_added: int = False
    for i in range(26):
        if (len(ans) == 0 or ans[-1] != chr(i+65)) and hash_map[i] > 0:
            ans += chr(i+65)
            hash_map[i] -= 1

            suffix_len: int = len(input_str) - len(ans)
            max_idx, max_freq = 0, 0
            for j in range(26):
                if hash_map[i] > max_freq:
                    max_idx, max_freq = i, hash_map[i]

            can_be_placed: bool = True
            if max_idx == i:
                can_be_placed = not (max_freq > suffix_len // 2)
            else:
                can_be_placed = not ( max_freq > (suffix_len + 1) // 2 )
            
            if not can_be_placed:
                ans = ans[:-1]
                hash_map[i] += 1
                continue

            char_added = True
            break

    if not char_added:
        print(-1)
        break

print(ans)
