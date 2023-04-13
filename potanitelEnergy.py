#Bir yayın ucuna m−2 kg bir kütke tutturulmuştur, yay sabiti k = 10 N/m dir, 
#ve başlangıç yerdeğiştirmesi x = 1.4m dir. Kütle salınıma başlamadan önce 
#sahip olduğu potansiye enerjiyi hesaplayan python kodu.

m = 2 # kütle, kg cinsinden
g = 9.81 # yerçekimi ivmesi, m/s^2 cinsinden
k = 10 # yay sabiti, N/m cinsinden
x = 1.4 # başlangıç yerdeğiştirme, m cinsinden

U = (1/2) * k * x**2
mgh = m * g * x

print("Potansiyel enerji (Joule):", U)