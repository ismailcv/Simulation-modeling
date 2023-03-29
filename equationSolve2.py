"""
bu denklemi çözen python kodu
1.1y - 3x - 0.9z = 3.61
4.7z - 4.1x - 0.17y = -42.527
2.9y + 2.2z - 1.1x = 3.87
"""

# sympy kütüphanesinden gerekli fonksiyonları içeri aktarın
from sympy import symbols, Eq, solve

# x, y ve z sembollerini tanımlayın
x, y, z = symbols('x y z')

# Denklemleri tanımlayın
eq1 = Eq(1.1*y - 3*x - 0.9*z, 3.61)
eq2 = Eq(4.7*z - 4.1*x - 0.17*y, -42.527)
eq3 = Eq(2.9*y + 2.2*z - 1.1*x, 3.87)

# Denklemleri çözün
sol = solve((eq1, eq2, eq3), (x, y, z))

# Sonuçları yazdırın
print("x =", sol[x])
print("y =", sol[y])
print("z =", sol[z])