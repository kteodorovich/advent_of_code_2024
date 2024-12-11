import math 

with open('input.txt', 'r') as f:
  grid = [list(l.strip()) for l in f.readlines()]

# get specific locs
antennas = {}
for i in range(len(grid)):
  for j in range(len(grid[i])):
    if grid[i][j] != '.':
      if grid[i][j] in antennas:
        antennas[grid[i][j]].append((i,j))
      else:
        antennas[grid[i][j]] = [(i,j)]

def inbounds(r,c,grid):
  return 0 <= r < len(grid) and 0 <= c < len(grid[r])

def place_antinode(r,c,grid):
  if inbounds(r,c,grid) and grid[r][c] != '#':
    grid[r][c] = '#'
    return 1
  return 0
    

# part 1
count = 0
antinodes = [['.' for _ in row] for row in grid]
for a in antennas:
  for i, a1 in enumerate(antennas[a]):
    for a2 in antennas[a][i+1:]:
      dx,dy = a2[0]-a1[0], a2[1]-a1[1]
      
      # in between
      if dx % 3 == 0 and dy % 3 == 0:
        count += place_antinode(a1[0] + dx//3, a1[1] + dy//3, antinodes)
        count += place_antinode(a1[0] + 2*dx//3, a1[1] + 2*dy//3, antinodes)

      # outside
      count += place_antinode(a1[0] - dx, a1[1] - dy, antinodes)
      count += place_antinode(a2[0] + dx, a2[1] + dy, antinodes)

print(count)
        
# part 2
def rel_prime(a, b):
  if a == 1 or b == 1:
    return None

  if a % b == 0:
    return b
    
  if b % a == 0:
    return a

  for i in range(2, min(a,b)):
    if a % i == 0 and b % i == 0:
      return i

  return None

def reduce_fraction(a,b):
  orig = a,b
  asign = 1 if a >= 0 else -1
  bsign = 1 if b >= 0 else -1

  a = abs(a)
  b = abs(b)

  factor = rel_prime(a,b)
  while factor is not None:
    a /= factor
    b /= factor
    factor = rel_prime(a,b)

  a *= asign
  b *= bsign
  #print('reduced', orig, 'to', (a,b))
  return a,b


count = 0
antinodes = [['.' for _ in row] for row in grid]
for a in antennas:
  for i, a1 in enumerate(antennas[a]):
    for a2 in antennas[a][i+1:]:
      dy,dx = a2[0]-a1[0], a2[1]-a1[1]
      dy,dx = reduce_fraction(dy,dx)

      # before a1
      r = a1[0]
      c = a1[1]
      while inbounds(r,c,grid):
        count += place_antinode(r,c,antinodes)
        r -= dy
        c -= dx

      # after a1
      r = a1[0]
      c = a1[1]
      while inbounds(r,c,grid):
        count += place_antinode(r,c,antinodes)
        r += dy
        c += dx

print(count)
        

