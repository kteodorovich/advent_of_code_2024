
with open('input.txt', 'r') as f:
  grid = [list(map(int, list(l.strip()))) for l in f.readlines()]


# part 1
def inbounds(i,j,grid):
  return 0 <= i < len(grid) and 0 <= j < len(grid[i])

def score(i,j,grid):
  if grid[i][j] == 9:
    return {(i,j)}

  s = set()
  n = grid[i][j]
  steps = [(-1,0), (0,1), (1,0), (0,-1)]
  for dy,dx in steps:
    if inbounds(i+dy,j+dx,grid) and grid[i+dy][j+dx] == n+1:
      s = s.union(score(i+dy,j+dx,grid))

  return s


s = 0
for i in range(len(grid)):
  for j in range(len(grid[i])):
    if grid[i][j] == 0:
      s += len(score(i,j,grid))

print(s)
    
# part 2
def rating(i,j,grid):
  if grid[i][j] == 9:
    return 1

  s = 0
  n = grid[i][j]
  steps = [(-1,0), (0,1), (1,0), (0,-1)]
  for dy,dx in steps:
    if inbounds(i+dy,j+dx,grid) and grid[i+dy][j+dx] == n+1:
      s += rating(i+dy,j+dx,grid)

  return s

s = 0
for i in range(len(grid)):
  for j in range(len(grid[i])):
    if grid[i][j] == 0:
      s += rating(i,j,grid)

print(s)
