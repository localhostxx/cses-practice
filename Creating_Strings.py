
def permutation(curr_str, curr_str_len, s, vis_array, ans_set):
    
    if curr_str_len == len(s):
        ans_set.add(curr_str)
        
    
    for i in range(len(s)):
        if vis_array[i]:
            continue
        vis_array[i] = True
        permutation(curr_str+s[i], curr_str_len+1, s, vis_array, ans_set)
        vis_array[i] = False

s = input()
vis_array = [False]*len(s)

ans = set()
permutation("", 0, s, vis_array, ans)

print(len(ans))
for ans_str in ans:
    print(ans_str)
