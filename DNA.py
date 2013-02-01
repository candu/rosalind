import sys
from collections import Counter

data = sys.stdin.read()
d = Counter()
for c in data:
  d[c] += 1
print d['A'], d['C'], d['G'], d['T']
