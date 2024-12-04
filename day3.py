import re

with open('input.txt', 'r') as f:
  txt = f.read()

pattern = 'mul\(\d{1,3},\d{1,3}\)'
s = 0

for m in re.findall(pattern, txt):
  n1, n2 = map(int, m[4:-1].split(','))
  s += n1 * n2

print(s)

s = 0
dos = re.finditer('do\(\)', txt)
donts = re.finditer("don\'t\(\)", txt)
mul = re.finditer(pattern, txt)
stuff = {}
for d in dos:
  stuff[d.start()] = 'do'

for d in donts:
  stuff[d.start()] = 'dont'

for m in mul:
  stuff[m.start()] = txt[m.start():m.end()]

count = True
for i in sorted(stuff.keys()):
  if stuff[i] == 'do':
    count = True
  elif stuff[i] == 'dont':
    count = False
  elif count:
    m = stuff[i]
    n1, n2 = map(int, m[4:-1].split(','))
    s += n1 * n2

print(s)




