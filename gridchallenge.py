def gridChallenge(grid):
    # Write your code here
    grid=[list(row) for row in grid]
    r=len(grid)
    c=len(grid[0])
    for i in range(r):
        grid[i].sort()
    for j in range(c):
        for i in range(1,r):
            if not grid[i-1][j]<=grid[i][j]:
                return "NO"
    return "YES"


# grid=['adc','ade','efg']
'''a b c
a d e
e f g
The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so the answer would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.'''
grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
'''abcde
fghij
klmno
pqrst
uvwxy'''
print(gridChallenge(grid))