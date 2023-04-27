#Klasik Sudoku oyunu için geçerli bir başlangıç durumunu oluşturacak python kodu
import random

# 9x9 boyutunda bir matris tanımlıyoruz
sudoku_board = [[0 for x in range(9)] for y in range(9)]

# Matrisin bazı hücrelerine rastgele değerler atıyoruz
for i in range(9):
    for j in range(9):
        num = (i*3 + i//3 + j) % 9 + 1
        sudoku_board[i][j] = num

# Rastgele birkaç hücrenin değerini silerek normal bir Sudoku tahtası oluşturuyoruz
num_of_cells_to_remove = 50  # oluşturulan tahtadan kaç hücrenin silineceğini belirliyoruz

for _ in range(num_of_cells_to_remove):
    while True:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if sudoku_board[row][col] != -1:
            break
    temp = sudoku_board[row][col]
    sudoku_board[row][col] = -1

    # Oluşturulan tahtanın doğruluğunu kontrol ediyoruz
    # Her bir satır, sütun ve 3x3 kutuda 1-9 arası sayılar sadece bir kez geçmeli
    # Her boş hücreye yalnızca bir sayı yerleştirilebilmeli
    is_valid = True
    for i in range(9):
        if (sudoku_board[row][i] == temp and i != col) or \
                (sudoku_board[i][col] == temp and i != row):
            is_valid = False
            break

    for i in range(row // 3 * 3, row // 3 * 3 + 3):
        for j in range(col // 3 * 3, col // 3 * 3 + 3):
            if (sudoku_board[i][j] == temp and i != row and j != col):
                is_valid = False
                break

    if not is_valid:
        sudoku_board[row][col] = temp

# Matrisi yazdırıyoruz
for i in range(9):
    print(sudoku_board[i])
