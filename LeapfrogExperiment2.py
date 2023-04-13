import matplotlib.pyplot as plt
import numpy as np

def Spring(niter):
    k = 10  # yay sabiti
    x = 1.4  # başlangıç yer değiştirme
    m = 2  # kütle
    v1 = 0  # başlangıç hızı
    dt = 0.5  # zaman adımı
    x1 = x
    xs = []
    ts = []
    vs = []
    for i in range(niter):
        a = -k * x1 / m
        v2 = v1 + a * dt
        x2 = x1 + v1 * dt + 0.5 * a * dt * dt
        v1 = v2 - 0.01 * v2
        x1 = x2
        xs.append(x2)
        vs.append(v2)
        ts.append(i)
    return ts, xs, vs

ts, xs, vs = Spring(200)
plt.plot(ts, xs, label="Konum")
plt.plot(ts, vs, label="Hız")
plt.xlabel("Zaman Adımı")
plt.ylabel("Konum / Hız")
plt.title("Sürtünmeli Yay Sistemi")
plt.legend()
plt.show()
