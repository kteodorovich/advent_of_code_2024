i = 0
with open('input.txt', 'r') as f:
  ids = []
  files = []
  empty = False
  for ch in f.read().strip():
    files.append([-1 if empty else i, int(ch)])
    ids += [-1 if empty else i] * int(ch)
    empty = not empty
    if empty:
      i += 1

# part 1
first_empty = ids.index(-1)
while first_empty < len(ids):
  ids[first_empty] = ids[-1]
  ids.pop(-1)
  while first_empty < len(ids) and ids[first_empty] != -1:
    first_empty += 1

count = sum([i*ids[i] for i in range(len(ids))])
print(count)

# part 2
#for f in files:
#  if f[0] != -1:
#    print(str(f[0])*f[1], end='')
#  else:
#    print('.'*f[1], end='')
#print()

idx = len(files) - 1
while idx >= 0 and files[idx][0] != -1:
  file = files[idx][:]
  # insert at leftmost possible empty space
  toplace = None
  for j, f in enumerate(files[:idx]):
    if f[0] == -1 and f[1] >= file[1]:
      toplace = j
      break
  
  if toplace is not None:
    files[idx][0] = -1
    files[toplace][1] -= file[1]
    if files[toplace][1] <= 0:
      files.pop(toplace)
    files.insert(toplace, file)

    # print
#    for f in files:
#      if f[0] != -1:
#        print(str(f[0])*f[1], end='')
#      else:
#        print('.'*f[1], end='')
#    print()
  else:
    idx -= 1
    if idx < 0:
      break

    
  while files[idx][0] == -1:
    idx -= 1

s = 0
i = 0
for f in files:
  for j in range(f[1]):
    if f[0] != -1:
      s += i * f[0]
    i += 1

print(s)
  
