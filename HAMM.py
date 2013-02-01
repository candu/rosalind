import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
dist = 0
for i, c in enumerate(s1):
  if c != s2[i]:
    dist += 1
print dist
