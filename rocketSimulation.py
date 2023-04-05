import matplotlib.pyplot as plt
import numpy as np


def InitLander():
    y1 = 1000  # yükseklik
    m1 = 15000  # roket kütlesi
    g = -9.8  # yerçekimi
    v1 = 0
    time = 0.0
    dt = 0.1  # simülasyonda kıllanılan zaman adımı
    force = 100000  # yanmanın ürettiği kuvvet (iki katına çıkartıldı)
    k = 100  # yanma esnasında kütle kayıp oranı
    return y1, v1, m1, g, time, dt, force, k


def RunLander(y1, v1, m1, g, time, dt, force, burns):
    #y1, v1, m1, g, time, dt, force, k=initvals
    vs, ys, acs = [], [], []
    ok = True
    while ok:
        aplus, m1 = Burn(time, m1, force, k, burns)
        y2, v2, accel = Iterate(g, y1, v1, aplus, dt)
        vs . append(v2)
        ys. append(y2)
        acs . append(accel)
        if m1 < 1000 or y2 <= 0:
            ok = False
        y1, v1 = y2, v2
        time += dt
    return ys, vs, acs


def Iterate(g, y1, v1, aplus, dt):
    accel = g + aplus
    v2 = v1 + accel * dt
    y2 = y1 + v1 * dt + 0.5 * accel * dt ** 2
    return y2, v2, accel


def Burn(time, m1, force, k, burns):
    aplus = 0
    for t1, d in burns:
        if t1 < time < t1 + d:
            aplus = force / m1
            m1 = m1 - k
            break
    return aplus, m1


def PlotLander(ys, vs, acs):
    ys1 = np.array(ys)/100.
    vs1 = np.array(vs)/5.
    plt. plot(np.zeros(len(ys1)))
    plt. plot(vs1, "-b", label="hiz")
    plt. plot(ys1, "-r", label="konum")
    plt. plot(acs, "-g", label="ivme")
    plt.legend(loc="upper left")
    plt. show()


initvals = InitLander()
y1, v1, m1, g, time, dt, force, k = initvals
burns = [(10, 2), (15, 2), (20, 3), (30, 3), (35, 3)]
ys, vs, acs = RunLander(y1, v1, m1, g, time, dt, force, burns)
#print (ys,vs, acs)
PlotLander(ys, vs, acs)
