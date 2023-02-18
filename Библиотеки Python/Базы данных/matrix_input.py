from config import filename

columns = []
data = []


def write_to_file(filename):
    """Запись БД в файл"""
    global columns, data
    with open(filename, 'w') as file:
        file.write(','.join(columns) + '\n')
        for line in data:
            line = [str(i) for i in line]
            file.write(','.join(line) + '\n')


def check_type(value, dt, index_i, index_j):
    """Сравниваем тип введённого значения с типом предыдущего значения в столбце
    True - сщвпадает, False - нет"""
    return isinstance(value, type(dt[index_i - 1][index_j]))


def type_definition(temp_name: str):
    """Определяем тип значения в столбце: int, str, float"""
    if temp_name.isdigit():
        return int(temp_name)
    if temp_name.replace('.', '', 1).isdigit():
        return float(temp_name)
    return str(temp_name)


def stop_input(value):
    print(80 * '-')
    print(f'ВВОД {value} СТОЛБЦОВ ОКОНЧЕН')
    print(80 * '-')


def input_matrix():
    """Ввод базы данных пользователем"""
    global columns, data
    col = int(input('Введите количество столбцов: '))
    for i in range(col):
        temp_name = input(f'Введите название {i + 1}-го столбца: ')
        columns.append(temp_name)
    stop_input('НАЗВАНИЙ')

    row = int(input('Введите количество строк: '))
    for i in range(row):
        data_temp = []
        for j in range(col):
            if i == 0:
                temp_name = type_definition(input(f'Введите значение столбца {columns[j]}: '))
            else:
                temp_name = type_definition(
                    input(f'Введите значение столбца {columns[j]}. Ожидаемый тип данных {type(data[i - 1][j])}: '))
                while not check_type(temp_name, data, i, j):
                    temp_name = type_definition(input(
                        f'Тип данных введённого значения не соответствует предыдущему типу данных значений в столбце'
                        f'\nПожалуйста, введите значение для столбца {columns[j]}, '
                        f'тип данных в котором соответствует {type(data[i - 1][j])}\nВвод: '))
            data_temp.append(temp_name)
        data.append(data_temp)

    stop_input('ЗНАЧЕНИЙ')
    write_to_file(filename)


def main():
    """Запуск программы"""
    yes_or_no = input('Хотите перезаписать базу данных?\n"y" - ДА, "n" - НЕТ\nВаш выбор: ')
    while yes_or_no.lower() not in ('y', 'n', 'н', 'т'):
        print('Пожалуйста, введите корректные данные.')
        yes_or_no = input('Хотите перезаписать базу данных?\n"y" - ДА, "n" - НЕТ\nВаш выбор: ')
    if yes_or_no.lower() in ('y', 'н'):
        input_matrix()
    else:
        print('Перезапись отменена\nПрограмма завершена')
        exit()


main()
