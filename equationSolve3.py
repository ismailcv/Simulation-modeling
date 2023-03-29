"""
ax + by = c
dx+ ey = f

a, b, d ve e değerleri için -1 ile 1 arasında rastgele sayılar üretin,
c ve f için rastgele değerler üretin,
x ve y değerini hesaplayın.
Bu işlemi yapan python kodu.
"""

import random

# a, b, d, e için rastgele sayılar oluşturma
a = random.uniform(-1, 1)
b = random.uniform(-1, 1)
d = random.uniform(-1, 1)
e = random.uniform(-1, 1)

# c ve f için rastgele sayılar oluşturma
c = random.uniform(-10, 10)
f = random.uniform(-10, 10)

# x ve y değerlerini hesaplama
x = (c - b * f / e) / (a - b * d / e)
y = (f - d * x) / e

print("x =", x)
print("y =", y)
