import random
import numpy as np


# Объявление класса колоды
class CharacterCard(object):
    def __init__(self, name, id, status, position, killer_status,
                 police_status):
        self.name = name
        self.id = id
        self.status = status
        self.position = position
        self.killer_status = killer_status
        self.police_status = police_status


def get_position(name):
    position = np.where(matrix == name)
    return int(position[0][0])*5 + int(position[1][0])

def get_information(deck:dict, name):
    information = [deck.get(name).name, deck.get(name).id, deck.get(name).status, deck.get(name).position ,deck.get(name).killer_status, deck.get(name).police_status]
    return information

def shift_row_right(matrix, row):
    matrix[row, :] = np.roll(matrix[row, :], 1)
    return matrix


def shift_row_left(matrix, row):
    matrix[row, :] = np.roll(matrix[row, :], -1)
    return matrix


def shift_column_right(matrix, column):
    matrix[:, column] = np.roll(matrix[:, column], 1)
    return matrix


def shift_column_left(matrix, column):
    matrix[:, column] = np.roll(matrix[:, column], -1)
    return matrix


# def kill_character(name):

# Создание колоды
CharacterDeck = {
    'Zachary': CharacterCard('Закари', 0, 0, 1, 0, 0),
    'Eliss': CharacterCard('Элисс', 1, 0, 2, 0, 0),
    'Barrin': CharacterCard('Бэррин', 2, 0, 3, 0, 0),
    'Clive': CharacterCard('Клайв', 3, 0, 4, 0, 0),
    'Deirdre': CharacterCard('Дейдра', 4, 0, 5, 0, 0),
    'Ernest': CharacterCard('Эрнест', 5, 0, 6, 0, 0),
    'Franklin': CharacterCard('Франклин', 6, 0, 7, 0, 0),
    'Geneva': CharacterCard('Женева', 7, 0, 8, 0, 0),
    'Horatio': CharacterCard('Горацио', 8, 0, 9, 0, 0),
    'Irma': CharacterCard('Ирма', 9, 0, 10, 0, 0),
    'Julian': CharacterCard('Джулиан', 10, 0, 11, 0, 0),
    'Christophe': CharacterCard('Кристоф', 11, 0, 12, 0, 0),
    'Linus': CharacterCard('Лайнус', 12, 0, 13, 0, 0),
    'Marion': CharacterCard('Мэрион', 13, 0, 14, 0, 0),
    'Neil': CharacterCard('Нейл', 14, 0, 15, 0, 0),
    'Ophelia': CharacterCard('Офелия', 15, 0, 16, 0, 0),
    'Phoebe': CharacterCard('Фиби', 16, 0, 17, 0, 0),
    'Quinton': CharacterCard('Куинтон', 17, 0, 18, 0, 0),
    'Ryan': CharacterCard('Райан', 18, 0, 19, 0, 0),
    'Simon': CharacterCard('Саймон', 19, 0, 20, 0, 0),
    'Trevor': CharacterCard('Тревор', 20, 0, 21, 0, 0),
    'Ulysses': CharacterCard('Улисс', 21, 0, 22, 0, 0),
    'Vladimir': CharacterCard('Владимир', 22, 0, 23, 0, 0),
    'William': CharacterCard('Вильгельм', 23, 0, 24, 0, 0),
    'Yvonne': CharacterCard('Ивонн', 24, 0, 25, 0, 0)}

# Создаем список с именами карт
values = CharacterDeck.values()
keys = CharacterDeck.keys()
data = []
for key in keys:
    data.append(key)

# Перемешаем карты в случайном порядке
random.shuffle(data)

# Сформируем поле карт 5х5
matrix = np.array(data).reshape(5, 5)
print(matrix)
# Сдвиг строки
print('ведите номер строки которую сдвинуть вправо')
row = int(input())
shift_row_right(matrix, row)
print(matrix)
# Сдвиг столбца
print('ведите номер столбца, который сдвинуть')
column = int(input())
shift_column_right(matrix, column)
print(matrix)

# Вычисляем координату элемента (строка, столбец)
print('ведите имя, которое ищите')
name = str(input())
print('номер позиции', get_position(name))
#Получаем информацию по имени
print(get_information(CharacterDeck, name))
#заменяем положение
CharacterDeck[name].position = get_position(name)
print(get_information(CharacterDeck, name))
