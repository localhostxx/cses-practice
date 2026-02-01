from collections import deque

n = int(input())

grid = [[-1 for _ in range(n)] for _ in range(n)] 
grid[0][0] = 0

jump_queue = deque()
jump_queue.append((0,0))

def check_inside_grid(cordinates):
    x, y = cordinates
    if  x < 0 or x >= n or y < 0 or y >= n:
        return False
    else:
        return True

def attack_squares(attack_cordinates, initial_cordinates):
    if check_inside_grid(attack_cordinates):
        ax, ay = attack_cordinates
        x, y = initial_cordinates
        if grid[ax][ay] == -1:
            grid[ax][ay] = grid[x][y] + 1
            jump_queue.append((ax, ay))
        else:
            grid[ax][ay] = min(grid[ax][ay], grid[x][y]+1)

def knight_attack(cordinates):
    x, y = cordinates

    attack_cordinates = [(x+2, y-1), (x+2, y+1), 
                      (x-2, y-1), (x-2, y+1), 
                      (x+1, y+2), (x-1, y+2), 
                      (x+1, y-2), (x-1, y-2)]

    for attack_cordinate in attack_cordinates:
        attack_squares(attack_cordinate, cordinates)
        
while len(jump_queue) != 0:
    cordinates = jump_queue.popleft()
    knight_attack(cordinates)

for row in grid:
    print(*row)
