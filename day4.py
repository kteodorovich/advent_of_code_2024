
def in_bounds(grid,r,c):
  return 0<=r<len(grid) and 0<=c<len(grid[r])

def find_target(grid, rs, cs, target='XMAS'):
  count = 0
  for R in range(len(grid)):
    for C in range(len(grid[R])):
      good = 1
      r, c = R, C
      for ch in target:
        if not in_bounds(grid,r,c) or grid[r][c] != ch:
          good = 0
          break

        r += rs
        c += cs

      count += good

  return count

# read input
with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

# part 1
count = 0
for rs in range(-1,2):
  for cs in range(-1,2):
    count += find_target(lines,rs,cs)

print(count)

# part 2
count = 0
for R in range(len(lines)-2):
  for C in range(len(lines[R])-2):
    if (((lines[R][C] == 'M' and lines[R+2][C+2] == 'S') or 
         (lines[R][C] == 'S' and lines[R+2][C+2] == 'M')) and
        ((lines[R+2][C] == 'M' and lines[R][C+2] == 'S') or 
         (lines[R+2][C] == 'S' and lines[R][C+2] == 'M')) and
         lines[R+1][C+1] == 'A'):

         count += 1

print(count)
