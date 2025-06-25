class WorkingWithFiles():

    def open_file():
        try:
                print('Example of input: matrix.txt ')
                filename = str(input("Filename - "))
        except ValueError:
                print('Incorrect input! Please enter an string.')

        matrix = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    try:
                        row = [int(x) for x in line.strip().split()]
                    except ValueError as e:
                        raise ValueError(f"Error in line {line_num}: {str(e)}") from e
                    
                    if not row:
                        raise ValueError("Empty row")
                        
                    matrix.append(row)
                
                if not matrix:
                    raise ValueError("Empty file")
                    
                first_row_len = len(matrix[0])
                for i, row in enumerate(matrix, 1):
                    if len(row) != first_row_len:
                        raise ValueError(f"Row {i} has a length {len(row)}, expected {first_row_len}")
                        
        except FileNotFoundError:
            raise FileNotFoundError(f"File don't find: {filename}")
        except IOError as e:
            raise IOError(f"File Read Error: {str(e)}") from e
            
        return matrix
    
    def save_matrix_to_txt(matrix: list, file_path: str) -> None:
    
        # Проверка на пустую матрицу
        if not matrix or not all(matrix):
            raise ValueError("Empty matrix")
        
        # Проверка одинаковой длины всех строк
        row_lengths = {len(row) for row in matrix}
        if len(row_lengths) != 1:
            raise ValueError("ValueError")

        # Определение максимальной ширины для каждого столбца
        cols = len(matrix[0])
        max_widths = [
            max(len(f"{num:.6f}".rstrip('0').rstrip('.') if isinstance(num, float) else str(num)) 
            for num in column)
            for column in zip(*matrix)
        ]

        # Запись в файл с выравниванием
        with open(file_path, 'w', encoding='utf-8') as file:
            for row in matrix:
                formatted_row = [
                    f"{num:.6f}".rstrip('0').rstrip('.') if isinstance(num, float) else str(num)
                    for num in row
                ]
                # Сборка строки с выравниванием
                line = " ".join(
                    element.rjust(width) 
                    for element, width in zip(formatted_row, max_widths)
                )
                file.write(line + '\n')
