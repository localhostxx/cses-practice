tcs = int(input())
for _ in range(tcs):
    n, a, b = (map(int, input().split()))
    
    if  a+b > n or (a == 0 or b == 0) and not (a==0 and b==0):
        print("NO")
    else:
        cards = [card+1 for card in reversed(range(a+b))]

        print("YES")
        
        winner, loser = ([], [])
            
        for i in range(a+b):
            winner.append(cards[i])
            loser.append(cards[(min(a,b)+i) % (a+b)])
        
        rem = n - (a + b)
        while rem > 0:
            winner.append(a+b+rem)
            loser.append(a+b+rem)
            rem -= 1
            
        if a < b:
            winner, loser = loser, winner
        print(*winner)
        print(*loser)
