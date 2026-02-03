import math
digit_count = []

# test_str = ""
# for i in range(1, 10**6):
#     test_str += str(i)

tcs = int(input())
for _ in range(tcs):
    query = int(input())
    
    digits_count = 0
    no_of_digits = 0
    last_power_digits = 0

    for power in range(20):
        digits_count += ( 10**(power+1) - 10**(power) )*(power+1)

        # print(digits_count)
        if query <= digits_count:
            no_of_digits = power + 1
            break
    
        last_power_digits = digits_count

    offset = math.ceil((query - last_power_digits) / no_of_digits)
    rem = ((query - last_power_digits)%no_of_digits)
    number = (10**(no_of_digits-1) - 1) + offset
    print(str(number)[rem-1])
    # print(test_str[query-1])
