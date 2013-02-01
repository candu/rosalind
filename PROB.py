import sys
import math
from collections import Counter

s = sys.stdin.readline().strip()
d = Counter(s)
gc = d['G'] + d['C']
at = len(s) - gc
A = map(float, sys.stdin.readline().strip().split())
for x in A:
  print gc * math.log10(x / 2) + at * math.log10((1 - x) / 2),
