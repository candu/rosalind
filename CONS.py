import sys

t = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
s = 'ACGT'
lines = [line.strip() for line in sys.stdin.readlines()]
P = []
for c in lines[0]:
  P.append([0, 0, 0, 0])
for line in lines:
  for i, c in enumerate(line):
    P[i][t[c]] += 1
cs = []
for p in P:
  max_j = 0
  for j, n in enumerate(p):
    if n > p[max_j]:
      max_j = j
  cs.append(s[max_j])
print ''.join(cs)
for c in 'ACGT':
  print '{0}:'.format(c),
  i = t[c]
  for p in P:
    print p[i],
  print
