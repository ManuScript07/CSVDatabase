from config import filename, data as dt, culumns as col


def print_data(max_size_column, data):
    """Вывод базы данных"""
    print(f'База данных из файла: <{filename}>')
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(str(data[i][j]).ljust(max_size_column[j]), end=' ')
        if i == 0:
            print()
        print()


def max_len(columns, data):
    data.insert(0, columns)
    max_size_column = []
    for i in range(len(data[0])):
        max_lenght = 0
        for j in range(len(data)):
            lenght = len(str(data[j][i]))
            if lenght > max_lenght:
                max_lenght = lenght
        max_size_column.append(max_lenght)

    print_data(max_size_column, data)


def read_to_file(filename):
    try:
        with open(filename, 'r') as file:
            columns = tuple(file.readline().strip().split(','))
            data = []
            for line in file:
                line = tuple(line.strip().split(','))
                data.append(line)
            max_len(columns, data)
    except FileNotFoundError:
        print('Файл не найден\nДанные базы данных заменены на временные.')
        max_len(col, dt)


read_to_file(filename)
