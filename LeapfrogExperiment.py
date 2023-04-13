import matplotlib.pyplot as plt
import numpy as np

def Leapfrog(niter):
    k = 10 # yay sabiti
    x = 1.4 # başlangıç yer değiştirme
    m = 2 # kütle
    v = 0 # başlangıç hızı
    dt = 0.5 # zaman adımı
    xs = [x]
    vs = [v]
    ts = [0]

    for i in range(1, niter+1):
        k = k * 0.99 # k değerinin %1 azaltılması
        x_half = x + v * dt / 2
        a = -k * x_half / m
        v = v + a * dt
        x = x + v * dt
        xs.append(x)
        vs.append(v)
        ts.append(i*dt)

    plt.plot(ts, xs, label='x')
    plt.plot(ts, vs, label='v')
    plt.xlabel('Zaman')
    plt.ylabel('x,v')
    plt.title('Leapfrog Yöntemi - Yayın Zamanla Zayıflaması')
    plt.legend()
    plt.show()

Leapfrog(400)
