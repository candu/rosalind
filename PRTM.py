import sys
import lib.mass

P = sys.stdin.readline().strip()
print sum(lib.mass.proteinMass(c) for c in P)
