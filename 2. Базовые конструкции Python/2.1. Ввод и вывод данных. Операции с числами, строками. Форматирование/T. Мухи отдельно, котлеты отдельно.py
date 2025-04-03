# x1 + x2 = n
# k1 * x1 + k2 * x2 = m * (x1 + x2)
# (k1 - m) * (n - x2) + (k2 - m) * x2 = 0
# (k1 - m) * n + (k2 - k1) * x2 = 0
# x2 = (m - k1) * n / (k2 - k1)
# x1 = n - x2 = n - (m - k1) * n / (k2 - k1) = n * (k2 - m) / (k2 - k1)

n, m, k1, k2 = int(input()), int(input()), int(input()), int(input())
print(n * (k2 - m) // (k2 - k1), (m - k1) * n // (k2 - k1))
