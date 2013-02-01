def Choose(n, m):
  t = n - m
  if m > t:
    return Choose(n, t)
  C = 1
  for i in range(1, m+1):
    C *= i + t
    C /= i
  return C
