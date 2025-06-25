import files_connector as fc



def main():
#   Главная функция приложения
    while True:
        try:
            # Создание матрицы
            matrix =fc.ProgramVisualization.get_matrix_creation_choice()
            if matrix is None:
                continue
                
            # Операции с матрицей
            fc.ProgramVisualization.get_operation_choice(matrix)
            
        except KeyboardInterrupt:
            print("\nProgram terminated by user")
            break
        except Exception as e:
            print(f"Critical error: {str(e)}")
            break

if __name__ == "__main__":
    main()