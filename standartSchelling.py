"""
Standart Schelling simülasyonu
Bu kod, öncelikle grid boyutunu, boşluk oranını ve lambda değerini belirleyen 
üç parametre alır. Ardından, grid adlı bir numpy dizisi oluşturulur ve 
belirtilen boşluk oranıyla rastgele birka nokta boşaltılır. Ardından, geri 
kalan tüm noktalar için rastgele iki farklı türde ajan oluşturulur. 
Daha sonra, Schelling modelini çalıştırmak için bir dizi döngü kullanılır.
Her bir adımda, her nokta için benzerlik hesaplanır ve benzerlik eşiği altında 
olan ajanlar, en düşük benzerlik puanına sahip boş bir noktaya taşınır. 
Son olarak, son durum grafiği çizilir.
"""
import numpy as np
import matplotlib.pyplot as plt
import random

# ızgara boyutu
n = 100

# boş hücre oranı (%1)
empty_ratio = 0.01

# sigma
sigma = 2

# tekrar sayısı
num_iterations = 10


# ızgara oluşturma ve boş hücreleri rastgele belirleme
grid = np.zeros((n, n))
empty_cells = random.sample(range(n*n), int(empty_ratio * n*n))
for cell in empty_cells:
    row = cell // n
    col = cell % n
    grid[row, col] = -1  # -1: boş hücre

# ızgarayı görüntüleme
plt.imshow(grid, cmap='binary')
plt.show()

# Schelling Modeli uygulama
for iteration in range(num_iterations):
    # rastgele dolu hücreleri seçme
    non_empty_cells = np.where(grid != -1)
    np.random.shuffle(non_empty_cells[0])
    np.random.shuffle(non_empty_cells[1])
    
    # dolu hücreleri tek tek tarayarak mutluluk seviyesini hesaplama
    for i, row in enumerate(non_empty_cells[0]):
        col = non_empty_cells[1][i]
        neighbors = []
        for j in range(max(0, row-sigma), min(n, row+sigma+1)):
            for k in range(max(0, col-sigma), min(n, col+sigma+1)):
                if grid[j, k] != -1:
                    neighbors.append(grid[j, k])
        same_type_neighbors = [n for n in neighbors if n == grid[row, col]]
        happiness = len(same_type_neighbors) / len(neighbors)
        if happiness < 0.5:
            # mutsuz hücreleri rastgele boş hücrelere taşıma
            empty_cells = np.where(grid == -1)
            np.random.shuffle(empty_cells[0])
            np.random.shuffle(empty_cells[1])
            for empty_row, empty_col in zip(empty_cells[0], empty_cells[1]):
                if (empty_row, empty_col) == (row, col):
                    continue
                if grid[empty_row, empty_col] == -1:
                    grid[empty_row, empty_col] = grid[row, col]
                    grid[row, col] = -1
                    break
    
    # ızgarayı güncelleme ve görselleştirme
    plt.imshow(grid, cmap='binary')
    plt.show()
