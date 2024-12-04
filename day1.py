
arr1 = []
arr2 = []
with open('input.txt', 'r') as f:
  for line in f.readlines():
    a, b = map(int, line.split())
    arr1.append(a)
    arr2.append(b)

arr1.sort()
arr2.sort()

# part 1
s = 0
for a,b in zip(arr1, arr2):
  s += abs(a - b)

print(s)

# part 2
s = 0
for i, n in enumerate(arr1):
  s += n * arr2.count(n)

print(s)

