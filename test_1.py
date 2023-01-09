#Задание 1
import os
import datetime


def logger(old_function):

    def new_function(*args, **kwargs):

        dt_now = datetime.datetime.now()
        func_name = old_function.__name__
        result = old_function(*args, **kwargs)

        with open('main.log', 'a', encoding='utf-8') as file:
            file.write(f'Date/time: {dt_now}\n'
                       f'Name: {func_name}\n'
                       f'Arguments: {args, kwargs}\n'
                       f'Result: {result}\n')

        return result

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)


    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b


    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


    #Задание 3 (Применение логгера к старому коду)
    @logger
    def old_hw_test():
        cook_book = {}
        with open('recipes.txt', 'rt', encoding='utf-8') as file:
            for i in file:
                dish = i.strip()
                ingredients = []
                ing_count = file.readline()
                for j in range(int(ing_count)):
                    ingr = file.readline()
                    ingredient_name, quantity, measure = ingr.strip().split(' | ')
                    ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
                blank_line = file.readline()
                cook_book.update({dish: ingredients})
        return cook_book

    old_hw_test()