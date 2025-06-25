
import files_connector as fc

class ProgramVisualization:
    
    @staticmethod
    def print_matrix(matrix):
    #   Вывод матрицы в консоль
        if not matrix:
            print("Matrix is empty")
            return
        for row in matrix:
            print(row)
    
    @staticmethod
    def get_matrix_creation_choice():
    #   Меню создания матрицы
        while True:
            try:
                print('\n=== Меню создания матрицы ===')
                print('1: жестко заданная матрица')
                print('2: задание с клавиатуры')
                print('3: создание случайной матрицы')
                print('4: из файла')
                print('0: выход')
                
                choice = input("ваш выбор: ").strip()
                
                if choice == '1':
                    return fc.MatrixCreator.create_predefined_matrix()
                elif choice == '2':
                    return fc.MatrixCreator.create_keyboard_matrix()
                elif choice == '3':
                    return fc.MatrixCreator.create_random_matrix()
                elif choice == '4':
                    return fc.WorkingWithFiles.open_file()
                elif choice == '0':
                    print("выход из программы...")
                    exit()
                else:
                    print("Неверный выбор, попробуйте еще раз!")
                    
            except (KeyboardInterrupt, EOFError):
                print("\nOperation cancelled")
                return None
            except Exception as e:
                print(f"Error: {str(e)}")
                return None

    @staticmethod
    def get_operation_choice(matrix):
    #   Меню операций с матрицей
        while True:
            try:
                print('\n=== Меню матричных операций ===')
                print('1: Сортировка матрицы')
                print('2: Транспорирование матрицы')
                print('3: Показать матрицу')
                print('4: Сохранить матрицу')
                print('5: Другие операции с матрицами и высчитывание интеграла')
                print('0: Вернуться в меню')
                     
                fst_choice = input("ваш выбор: ").strip()
               
                if fst_choice == '1':
                    sorted = fc.MatrixSorter()
                    matrix = sorted.sort_matrix(matrix)
                elif fst_choice == '2':
                    matrix = fc.MatrixTransformer.transpose(matrix)
                elif fst_choice == '3':
                    ProgramVisualization.print_matrix(matrix)
                elif fst_choice == '4':
                    print("Напиши имя файла, например: matrix_output.txt ")
                    try:
                        file_name = str(input())
                    except ValueError:
                        print('Name error')
                    fc.WorkingWithFiles.save_matrix_to_txt(matrix, file_name)
                elif fst_choice == '5':
                    while True:
                        print('\n=== другие операции с матрицами и высчет интеграла 17  ===')
                        print('1: (row - 7,col - 7) , Найдите минимальный и максимальный элементы в строке N, в столбце M.')
                        print('2: (row - 7,col - 7) , Подсчитайте количество четных и нечетных чисел в строке N, в столбце M.')
                        print('3: (A - 6.5,B - 17) , Найдите, на сколько элементов матрицы больше некоторого числа A и меньше некоторого числа B.')
                        print('4: (row - 7, A - 6.5, B - 17, m - 21, C - -18  ) Умножьте строку N матрицы на число A, вычтите число k*B, добавьте число m*C.')
                        print('5: Решите интеграл: x * e^x in the range from 0 to 1')
                        print('0: Вернуться назад')
                        
                        sec_choice = input("Ваш выбор: ").strip()

                        if sec_choice == '1':
                            print('Найти в строке(1)/столбце(2)')
                            choice = str(input())
                            if choice == '1':
                                print('Введите свою строку, в которой вы хотите найти эти элементы')
                                input_row = int(input())
                                fc.MatrixOperation.find_min_max_in_row(matrix, input_row)
                            elif choice == '2':
                                print('Введите свою строку, в которой вы хотите найти эти элементы')
                                input_col = int(input())
                                fc.MatrixOperation.find_min_max_in_column(matrix, input_col)
                            else:
                                print('Неверное значение')
                        elif sec_choice == '2':
                            print('Cout in row(1)/col(2)')
                            choice = str(input())
                            if choice == '1':
                                print('Введите свою строку, в которой вы хотите подсчитать количество этих элементов')
                                input_row = int(input())
                                fc.MatrixOperation.count_even_odd_in_row(matrix, input_row)
                            elif choice == '2':
                                print('Введите свой col, если вы хотите подсчитать эти элементы')
                                input_col = int(input())
                                fc.MatrixOperation.count_even_odd_in_column(matrix, input_col)
                            else:
                                print('Неверное значение')
                        elif sec_choice == '3':
                            print('Введите свои A и B')
                            value_A = float(input('A- '))
                            value_B = int(input('B- '))
                            fc.MatrixOperation.count_elements_greater_than(matrix, value_A)
                            fc.MatrixOperation.count_elements_less_than(matrix, value_B)
                        elif sec_choice == '0':
                            break
                        elif sec_choice == '4':
                            row = int(input('Введите вашу строку- ' ))
                            value_A = float(input('Введите значение A- ' ))
                            value_B = int(input('Введите значение B- ' ))
                            value_m = int(input('Введите значение m- ' ))
                            value_C = int(input('Введите значение C- ' ))
                            fc.MatrixOperation.modify_matrix_row(matrix, row,value_A,value_B,value_m,value_C)
                        elif sec_choice == '5':
                            fc.MatrixOperation.calculate_integral()
                elif fst_choice == '0':
                    return
                else:
                    print("Неверный выбор, попробуйте еще раз!")
                    
            except (KeyboardInterrupt, EOFError):
                print("\nOperation cancelled")
                return
            except Exception as e:
                print(f"Error: {str(e)}")
