import matplotlib.pyplot as plt
import numpy as np

def Spring (niter) :
    k = 10 # yay sabiti
    x = 1.4 # baslangin gerilmesi
    m = 2 # kutle
    v1 = 0 # baslangic hizi
    dt = 0.5 # zaman adimi
    x1 = x
    xs=[]
    ts=[]
    vs=[]
    for i in range (niter) :
        a = -k * x1 / m
        v2 = v1 + a * dt
        x2 = x1 + v1 * dt + 0.5 * a * dt * dt
        v1 = v2
        x1 = x2
        xs.append(x2)
        vs.append(v2)
        ts.append(i)
        #print ( i , x2 )
    return ts,xs,vs

niter=200
ts,xs,vs=Spring(niter)

# kütlenin hızı hesaplanıyor
v = vs[-1]
print("Kütlenin hızı:", v)

# enerji hesaplanıyor
k = 10 # yay sabiti
x = 1.4 # baslangin gerilmesi
m = 2 # kutle
E_p = 0.5 * k * x**2 # potansiyel enerji
E_k = 0.5 * m * v**2 # kinetik enerji
E = E_p + E_k # toplam enerji
print("Toplam enerji:", E)
