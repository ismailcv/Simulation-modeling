# 2. ödev bağımsız olasılık sorusu
# İsmail Can Varlı    

# random modülünü import ediyoruz
import random

# kullanıcıdan borunun uzunluğu, canlının tek seferde ilerleyebileceği uzunluk ve kaç kere hareket edeceği bilgilerini alıyoruz
a = int(input("Borunun uzunluğu: "))
x = int(input("Canlının tek seferde ilerleyebileceği uzunluk: "))
y = int(input("Kaç kere hareket edecek: "))

# canlı başlangıçta borunun ortasında bulunuyor
n = a // 2

# kullanıcının girdiği değerleri yazdırıyoruz
print(f"\nBorunun uzunluğu: {a}, Canlının tek seferde ilerleyebileceği uzunluk: {x}, Kaç kere hareket edecek: {y}\n")

# simülasyon sayısı ve toplam uzaklık değişkenlerini tanımlıyoruz
num_simulations = 10
total_distance = 0

# belirlenen sayıda simülasyon yapmak için for döngüsü kullanıyoruz
for sim in range(num_simulations):
    # her simülasyon başlangıcında canlı borunun ortasında bulunuyor
    n = a // 2
    
    # simülasyonun başladığına dair bir mesaj yazdırıyoruz
    print(f"Simülasyon {sim+1} başlıyor...")
    
    # belirtilen sayıda adım atmak için for döngüsü kullanıyoruz
    for i in range(y):
        # canlı borunun sonuna veya başına ulaştığında, diğer tarafından devam etmesi için işlem yapılıyor
        if n <= 0:
            n += a
        elif n >= a:
            n -= a

        # canlının hangi yönde hareket edeceğini rastgele seçiyoruz
        direction = random.choice([-1, 1])
        n += direction * x

        # canlının yeni konumunu ve hangi yöne gittiğini yazdırıyoruz
        print(f"{i+1}. konum: {n}, {'' if direction == 1 else 'sol'} tarafa gidiyor")

    # canlının başlangıç noktasına olan uzaklığını hesaplıyoruz
    distance = abs(n - a//2)
    total_distance += distance

    # simülasyon sonucunu yazdırıyoruz
    print(f"\nSimülasyon {sim+1} tamamlandı. Başlangıç noktasına olan uzaklık: {distance}\n")

# simülasyonların ortalamasını hesaplayıp yazdırıyoruz
average_distance = total_distance / num_simulations

print(f"Simülasyonların ortalaması: {average_distance}")
