
with open('input.txt', 'r') as f:
  lines = f.readlines()

def possible(curr, nums, target, firstop):
  if curr is None:
    if len(nums) == 0:
      return False

    if firstop == '+':
      curr = 0
    elif firstop == '*':
      curr = 1
  
  if len(nums) > 0:
    curr = eval(str(curr) + firstop + str(nums[0]))
    nums.pop(0)
  else:
    return curr == target

  return (possible(curr, nums[:], target, '+') or
          possible(curr, nums[:], target, '*') or
          possible(curr, nums[:], target, ''))
  
  
# part 1
count = 0
for line in lines:
  val, nums = line.split(':')
  val = int(val)
  nums = list(map(int, nums.split()))
  if (possible(None, nums, val, '+') or
      possible(None, nums, val, '*')):
      count += val

print(count)

