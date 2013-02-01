import sys
import lib.codon

s = sys.stdin.readline().strip()
print ''.join(filter(None, [lib.codon.acid(s[i:i+3]) for i in xrange(0, len(s), 3)]))
