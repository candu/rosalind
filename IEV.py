import sys

line = sys.stdin.readline().strip()
E = [2.0, 2.0, 2.0, 1.5, 1.0, 0.0]
A = map(int, line.split())
x = sum(e * a for (e, a) in zip(E, A))
print x
