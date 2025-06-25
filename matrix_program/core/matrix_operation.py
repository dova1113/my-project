
class MatrixSorter:
    def sort_matrix(self, matrix):
        # Сортирует матрицу по выбранному пользователем направлению и порядку.
        direction = self._get_sort_direction()
        order = self._get_sort_order()
        reverse = order == "2"

        if direction == "1":
            return self._sort_rows(matrix, reverse)
        else:
            return self._sort_columns(matrix, reverse)

    def _get_sort_direction(self):
    #   Запрашивает у пользователя направление сортировки.
        print("Выбор направления сортировки:")
        print("1. По строкам")
        print("2. По колонкам")
        while True:
            try:
                choice = input("Укажите свой выбор: ")
            except ValueError:
                print('Неверный ввод. Попробуйте еще раз.')
            if choice in ("1", "2"):
                return choice
            print("Неверный ввод. Попробуйте еще раз.")

    def _get_sort_order(self):
    #   Запрашивает у пользователя порядок сортировки.
        print("Выберите порядок сортировки:")
        print("1. По возрастанию")
        print("2. По убыванию")
        while True:
            try:
                choice = input("Укажите свой выбор: ")
            except ValueError:
                print('Неверный ввод. Попробуйте еще раз.')
            if choice in ("1", "2"):
                return choice
            print("Неверный ввод. Попробуйте еще раз.")

    def _sort_rows(self, matrix, reverse):
    #   Сортирует каждую строку матрицы.
        return [sorted(row, reverse=reverse) for row in matrix]

    def _sort_columns(self, matrix, reverse):
    #   Сортирует каждый столбец матрицы.
        transposed = list(zip(*matrix))
        sorted_transposed = [sorted(list(col), reverse=reverse) for col in transposed]
        sorted_matrix = list(zip(*sorted_transposed))
        return [list(row) for row in sorted_matrix]
class MatrixTransformer:
    @staticmethod
    def transpose(matrix):
    #   Транспонирует матрицу, меняя строки и столбцы местами

        # Проверка на пустую матрицу
        if not matrix:
            return []

        # Проверка что все строки имеют одинаковую длину
        row_length = len(matrix[0])
        for row in matrix:
            if len(row) != row_length:
                raise ValueError("ValueError")

        # Создание транспонированной матрицы через list comprehension
        return [[row[i] for row in matrix] for i in range(row_length)]
    
class MatrixOperation:
    @staticmethod
    def find_min_max_in_row(matrix, n):
        #Находит минимальный и максимальный элементы в строке N.
        
        row = matrix[n - 1]
        print(f'минимум в колонне {n} - {min(row)}, максимальное значение в столбце {n} - {max(row)}')
        return None
    @staticmethod
    def find_min_max_in_column(matrix, m):
        #Находит минимальный и максимальный элементы в столбце M.

        column = [row[m - 1] for row in matrix]
        print(f'минимум в колонне {m} - {min(column)}, максимальное значение в столбце {m} - {max(column)}')
        return None
    
    def count_even_odd_in_row(matrix, n):
        # Подсчитывает количество четных и нечетных чисел в строке N.
        
        even = 0
        odd = 0
        for num in matrix[n-1]:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        print(f"Row {n}: Even = {even}, Odd = {odd}")
        return None

    def count_even_odd_in_column(matrix, m):
        # Подсчитывает количество четных и нечетных чисел в столбце M.
        
        even = 0
        odd = 0
        for row in matrix:
            num = row[m-1]
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        print(f"Column {m}: Even = {even}, Odd = {odd}")
        return None
    def __init__(self, matrix):
        self.matrix = matrix

    def count_elements_greater_than(matrix, a):
    #   Подсчет элементов матрицы, строго больших заданного числа A.
        count = 0
        for row in matrix:
            for element in row:
                if element > a:
                    count += 1
        print(f'count of element greater than A - {count}')
        return None

    def count_elements_less_than(matrix, b):
    #   Подсчет элементов матрицы, строго меньших заданного числа B.
        count = 0
        for row in matrix:
            for element in row:
                if element < b:
                    count += 1
        print(f'count of element Less than B - {count}')
        return None
    
    def modify_matrix_row(matrix, row, A, B, m, C):
        import math
        row = row - 1
        k = (math.log(3)) ** 3  # Вычисляем k как куб натурального логарифма от 3
        for i in range(len(matrix[row])):
            # Применяем операцию к каждому элементу строки
            matrix[row][i] = matrix[row][i] * A - k * B + m * C
        return matrix

    def calculate_integral():
        from scipy.integrate import quad
        import math

        #   решите интеграл: x * e^x in the range from 0 to 1
        def integrand(x):
            return x * math.exp(x)
        
        lower_limit = 0
        upper_limit = 1
        #upper_limit = 1
        
        result, error = quad(integrand, lower_limit, upper_limit)
        print(f"Результат интегрального вырожения: {result:.4f}")
