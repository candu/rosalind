import sys
from lib.discrete import Choose

line = sys.stdin.readline().strip()
k, N = map(int, line.split())
t = 1 << k
print sum(Choose(t, i) * 0.25**i * 0.75**(t - i) for i in range(N, t+1))
