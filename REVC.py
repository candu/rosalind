import sys

data = sys.stdin.read().strip()
t = {
  'A': 'T',
  'T': 'A',
  'C': 'G',
  'G': 'C'
}
print ''.join(t[c] for c in data[::-1])
