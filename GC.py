import sys

db = {}
last = None
gc, n = 0, 0
for line in sys.stdin:
  line = line.strip()
  if line.startswith('>'):
    if last is not None:
      db[last] = 100.0 * gc / n
    last = line[1:]
    gc, n = 0, 0
  else:
    for c in line:
      if c == 'G' or c == 'C':
        gc += 1
      n += 1
if last is not None:
  db[last] = 100.0 * gc / n
L = sorted((v, k) for k, v in db.iteritems())
best_gc = L[-1]
print best_gc[1]
print best_gc[0]
