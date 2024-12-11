
def out_of_bounds(r, c, grid):
  return not (0 <= r < len(grid)) or not (0 <= c < len(grid[r]))


with open('input.txt', 'r') as f:
  lines = f.readlines()

grid = [list(l.strip()) for l in lines]
startr, startc = -1,-1

for i in range(len(grid)):
  for j in range(len(grid[i])):
    if grid[i][j] == '^':
      startr, startc = i,j

dirs = [(-1,0),(0,1),(1,0),(0,-1)]

# part 1
#d = 0
#vd,hd = dirs[d]
#count = 0
#r,c = startr, startc
#while True:
#  if out_of_bounds(r, c, grid):
#    break
#
#  while not out_of_bounds(r+vd, c+hd, grid) and grid[r+vd][c+hd] == '#':
#    d = (d + 1) % 4
#    vd,hd = dirs[d]
#
#  if grid[r][c] != 'X':
#    count += 1
#    grid[r][c] = 'X'
#  r += vd
#  c += hd
#
#
#print(count)

def makes_cycle(r, c):
  global dirs, startr, startc, grid
  if grid[r][c] == '#' or grid[r][c] == '^':
    return False # already has obstacle

  d = 0
  vd,hd = dirs[d]

  g = [r[:] for r in grid] # make grid copy
  g[r][c] = '#' # place extra obstacle
  r = startr
  c = startc

  while not out_of_bounds(r,c,g):
    # turn right while obstacle in way
    while not out_of_bounds(r+vd, c+hd, g) and g[r+vd][c+hd] == '#':
      d = (d + 1) % 4
      vd,hd = dirs[d]
    
    # if already visited this square going in same dir
    if 'urdl'[d] in g[r][c]:
      return True

    g[r][c] += 'urdl'[d]
    r += vd
    c += hd
  
  return False
  
# part 2 brute force ew
count = 0
for i in range(len(grid)):
  for j in range(len(grid[i])):
    if makes_cycle(i,j):
      count += 1

print(count)

