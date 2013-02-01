import sys

line = sys.stdin.readline().strip()
k, m, n = map(float, line.split())
t = k + m + n
pr_aa = (m * (m - 1) + 4 * m * n + 4 * n * (n - 1)) / (4 * t * (t - 1))
print 1.0 - pr_aa
