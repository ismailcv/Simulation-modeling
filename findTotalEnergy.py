#Bir cisim 1.5 m yükseklikteki bir platformdan 4.5 m/s'lik
#ilk hız ile 35 derece açı ile fırlatılıyor. Cismin başlangıçtaki
#ve tepe noktasında iken toplam enerjisini bulun python kodu

import math

height = 1.5 # yükseklik
velocity = 4.5  # ilk hız
angle = 35 # Açı
mass = 0.1 # Kütle
g = 9.81 # Yer çekimi ivmesi

# Açıyı dereceden radyana çeviriliyor
angle_rad = math.radians(angle)

# Maksimum yükseklik
max_height = height + ((velocity**2) * math.sin(angle_rad)**2) / (2 * g)
print("Maksimum yükseklik: ", max_height, "m")

# Başlangıçtaki kinetik enerji
start_ke = (1/2) * mass * velocity**2
print("Başlangıçtaki kinetik enerji: ", start_ke, "J")

# Başlangıçtaki potansiyel enerji
start_pe = mass * g * height
print("Başlangıçtaki potansiyel enerji: ", start_pe, "J")

# Tepe noktasındaki kinetik enerji
max_ke = (1/2) * mass * (velocity * math.cos(angle_rad))**2
print("Tepe noktasındaki kinetik enerji: ", max_ke, "J")

# Tepe noktasındaki potansiyel enerji
max_pe = mass * g * max_height
print("Tepe noktasındaki potansiyel enerji: ", max_pe, "J")

# Başlangıçtaki toplam enerji
start_e = start_ke + start_pe
print("Başlangıçtaki toplam enerji: ", start_e, "J")

# Tepe noktasındaki toplam enerji
max_e = max_ke + max_pe
print("Tepe noktasındaki toplam enerji: ", max_e, "J")

