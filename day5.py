from functools import cmp_to_key

with open('input.txt', 'r') as f:
  lines = f.readlines()

graph = {}

for i, line in enumerate(lines):
  if line.strip() == '':
    k = i
    break

  a,b = map(int, line.split('|'))
  if a in graph:
    graph[a].append(b)
  else:
    graph[a] = [b]

def compare(a, b):
  global graph

  if a in graph and b in graph[a]:
    return 1
  if b in graph and a in graph[b]:
    return -1
  return 0

updates = [list(map(int, line.split(','))) for line in lines[k+1:]]
fixed = []
s = 0
for i, update in enumerate(updates):
  if all([compare(update[i], update[i+1])>=0 for i in range(len(update)-1)]):
    s += update[len(update)//2]
  else:
    fixed.append(sorted(update, key=cmp_to_key(compare)))

print(s)

# part 2
s = 0
for update in fixed:
    s += update[len(update)//2]

print(s)
    
