
import random

class MatrixCreator:

    @staticmethod
    def create_predefined_matrix():
        return [[ 1, 2, 3, 4, 5, 6, 7  ],
                [ 1, 2, 3, 4, 5, 6, 7  ],
                [ 1, 2, 3, 4, 5, 6, 7  ],
                [ 1, 2, 3, 4, 5, 6, 7  ],
                [ 1, 2, 3, 4, 5, 6, 7  ],
                [ 1, 2, 3, 4, 5, 6, 7  ],
                [ 1, 2, 3, 4, 5, 6, 7  ]] # Реализация создания готовой матрицы
    @staticmethod
    def create_keyboard_matrix():
        # Реализация ручного ввода матрицы
        while True:
            try:
                rows = int(input("Введите количество строк: "))
                cols = int(input("Введите количество столбцов: "))
                break
            except ValueError:
                print('Неверный ввод! Пожалуйста, введите целое число.')

        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                while True:
                    try:
                        value = int(input(f"Введите элимент [{i}][{j}]: "))
                        row.append(value)
                        break
                    except ValueError:
                        print("Неверный ввод! Пожалуйста, введите целое число.")
            matrix.append(row)
        
        return matrix
    
    @staticmethod
    def create_random_matrix():
        # Реализация генерации случайной матрицы
        while True:
            try:
                rows = int(input("Введите количество строк: "))
                cols = int(input("Введите количество столбцов: "))
                size = random.randint(rows, cols)
                break
            except ValueError:
                print('Неверный ввод! Пожалуйста, введите целое число..')

        return [[random.random() for i in range(size)] 
                for i in range(size)]
    