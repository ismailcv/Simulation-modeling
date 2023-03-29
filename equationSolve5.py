"""
Efe’nin 30 tane madeni parası var. 1 kuruş, 5 kuruş, 10 kuruş ve 25 kuruşlardan
oluşmaktadır. Toplam parası 3,92 TL’dir. 10 kuruşların adeti 1 kuruşlardan 
bir fazladır. 10 kuruşların ve 25 kuruşların
toplam adeti 15’dir. Efe, her bir kuruş paradan kaç taneye sahiptir?
Bu problemi çözen python kodu
"""

total_amount = 392
num_of_coins = 30

# 10 kuruşluk madeni para sayısının x olduğunu ve 1 kuruşluk 
#madeni para sayısının x-1 olduğunu varsayalım
x = (num_of_coins + 1) // 2

# denklemi yazarsak  10x + 25(15 - x - 1) + 5(2x) + 1(x-1) = 392
num_of_10_coins = x
num_of_25_coins = 15 - x - 1
num_of_5_coins = 2 * x
num_of_1_coins = x - 1

print("1 Kuruşların sayısı:", num_of_1_coins)
print("5 Kuruşların sayısı:", num_of_5_coins)
print("10 Kuruşların sayısı:", num_of_10_coins)
print("25 Kuruşların sayısı:", num_of_25_coins)


