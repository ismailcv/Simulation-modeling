# hafta 4 ödev 
"""
4x + 2y =14
y - x =-5 
denklemini çözen python kodu
"""

# Denklemi çözmek için sympy kütüphanesini yükleyin
#!pip install sympy

# sympy kütüphanesinden gerekli fonksiyonları içeri aktarın
from sympy import symbols, Eq, solve

# x ve y sembollerini tanımlayın
x, y = symbols('x y')

# Denklemleri tanımlayın
eq1 = Eq(4*x + 2*y, 14)
eq2 = Eq(y - x, -5)

# Denklemleri çözün
sol = solve((eq1, eq2), (x, y))

# Sonuçları yazdırın
print("x =", sol[x])
print("y =", sol[y])
