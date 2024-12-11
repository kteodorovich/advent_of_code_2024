from functools import cache

with open('input.txt', 'r') as f:
  stones = list(map(int, f.read().strip().split()))

@cache
def blink(n, b):
  if b <= 0:
    return 1

  if n == 0:
    return blink(1, b-1)
  elif len(str(n)) % 2 == 0:
    s = str(n)
    return blink(int(s[:len(s)//2]), b-1) + blink(int(s[len(s)//2:]), b-1)
  
  return blink(n*2024, b-1)

num_blinks = 75
out = 0
for s in stones:
  out += blink(s, num_blinks)
print(out)
