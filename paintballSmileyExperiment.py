#Fizikteki Paintball Smiley sorusu
import math

d = 35    # mesafe
h = 25    # yükseklik
v = 100   # hız
theta = math.atan(h/d)
print(theta, math.degrees(theta))

vxp0 = v * math.cos(theta)
vyp0 = v * math.sin(theta) 
print(vxp0, vyp0)

print('Test için hız:', math.sqrt(vxp0**2 + vyp0**2))

t = d / vxp0
print('Uçuş süresi = ', t)

g = -9.8
hp1 = 0
hp2 = hp1 + vyp0 * t + 0.5 * g * t ** 2 
print('Merminin yüksekliği = ' , hp2)
      
vsy1 = 0
ys1 = h
ys2 = ys1 + vsy1 * t + 0.5 * g * t ** 2
print("Smiley'nin yüksekliği = " , ys2)
