
def adj_good(report, inc, i, j):
  if i<0 or j<0 or i>=len(report) or j>=len(report):
    return True

  return ((1 <= abs(report[i] - report[j]) <= 3) and
          ((inc and report[i] < report[j]) or
          (not inc and report[i] > report[j])))

def report_good(report, inc):
  if len(report) <= 1:
    return True

  for i in range(1, len(report)):
    if not adj_good(report, inc, i-1, i):
      return False

  return True

def report_good_with_skip(report, inc):
  if len(report) <= 1:
    return True

  for i in range(1, len(report)):
    if not adj_good(report, inc, i-1, i):
        if adj_good(report,inc,i-2,i) and report_good(report[i:], inc):
          return True
        elif adj_good(report,inc,i-1,i+1) and report_good(report[i+1:], inc):
          return True
        return False

  return True

with open('input.txt', 'r') as f:
  reports = [list(map(int, line.split())) for line in f.readlines()]

# part 1
num = 0
for report in reports:
  if report_good(report, inc=True) or report_good(report, inc=False):
    num += 1

print(num)
      
# part 2
num = 0
for report in reports:
  if report_good_with_skip(report, inc=True) or report_good_with_skip(report, inc=False):
    num += 1

print(num)
