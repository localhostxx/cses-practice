
chessboard = []
spread_cordinates = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

for _ in range(8):
    chessboard.append(list(input()))

def check_in_grid(cordinates):
    x, y = cordinates
    if x < 0 or x > 7 or y < 0  or y > 7:
        return False
    return True

def mark_attack(cordinates):
    for spread in spread_cordinates:
        x, y = cordinates
        while check_in_grid((x+spread[0], y+spread[1])):
            nx, ny = x+spread[0], y+spread[1]
            if chessboard[nx][ny] == '8':
                return False
            x, y = nx, ny
    return True

def place_queens(row, queens):
    if row == 8 and queens == 8:
        return 1
    
    ans = 0 
    for j in range(8):
        if chessboard[row][j] == '.' and mark_attack((row, j)):
            chessboard[row][j] = '8'
            ans += place_queens(row+1, queens+1)
            chessboard[row][j] = '.'

    return ans 

print(place_queens(0, 0))
