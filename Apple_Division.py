n = int(input())
weights = list(map(int, input().split()))

total_weight = sum(weights)

def subset(weights, current_sum, total_weight, idx, n):
    
    if idx == n - 1:
        return abs(current_sum - abs(current_sum - total_weight))

    included_weight = subset(weights, current_sum+weights[idx], total_weight, idx+1, n)
    not_included_weight = subset(weights, current_sum, total_weight, idx+1, n)

    return min(included_weight, not_included_weight)

print(int(subset(weights, 0, total_weight, 0, n)))
