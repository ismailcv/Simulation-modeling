"""
Efe’nin 30 tane madeni parası vardır ve bunlar 5 ve 10 kuruşlardan oluşmaktadır.
Efe’nin toplam parası 2,45 TL’dir. Efe’nin kaç tane 10 kuruşu ve kaç tane 
5 kuruşu vardır? Bu problemi çözen python kodu
"""

for x in range(31):
    for y in range(31):
        if x + y == 30 and 0.10*x + 0.05*y == 2.45:
            print("Efe'nin", x, "tane 10 kuruşu ve", y, "tane 5 kuruşu vardır.")