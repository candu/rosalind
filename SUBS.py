import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
i = s.find(t)
while i != -1:
  print i+1,
  i = s.find(t, i+1)
print
