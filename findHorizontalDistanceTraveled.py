#Bir cisim 1.5 m yükseklikteki bir platformdan 4.5 m/s lik
#ilk hız ile 35 derecelik açı altında fırlatılıyor. 
#Yere değdiği zaman yatayda ne kadar yol aldığını bulan
#python kodu.

import math

height = 1.5 # yükseklik
velocity = 4.5  # ilk hız
angle = 35 # Açı
g = 9.81 # Yer çekimi ivmesi

# Açıyı dereceden radyana çeviriliyor
angle_rad = math.radians(angle)

# Düşme süresini hesapla
time_of_flight = 2 * velocity * math.sin(angle_rad) / g

# Yatay mesafeyi hesapla
horizontal_distance = velocity * math.cos(angle_rad) * time_of_flight

print("Yatayda alınan mesafe: ", horizontal_distance, "m")