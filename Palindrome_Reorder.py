input_str = input()
char_dict = dict()

for char in input_str:
    if char_dict.get(char) == None:
       char_dict[char] = 0
    
    char_dict[char] += 1

flag, no_sol = False, False
odd_char = ''
ans_str = ""
for k in char_dict:
    if char_dict[k]%2 == 1:
        if flag:
            no_sol = True 
            break
        else:
            flag = True
            char_dict[k] -= 1
            odd_char = k
    
    ans_str += (k * (char_dict[k]//2))
    
if no_sol:   
    print("NO SOLUTION")
else:
    print(ans_str + odd_char + ans_str[::-1])
