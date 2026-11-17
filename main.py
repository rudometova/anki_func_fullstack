# import random
import sys
# import time
# from typing import Dict, Tuple


STOP_WORD = 'СТОП'


def load_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            words = {}
            for line in file:
                line = line.strip()
                if ',' in line:
                    parts = line.split(',', 1)
                    if len(parts) == 2:
                        word, translation = parts
                        words[word.strip()] = translation.strip()
            return words
    except FileNotFoundError:
        print(f'Ошибка: файл {filename} не найден.')
        sys.exit(1)


def save_words(words, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for word, translation in words.items():
            file.write(f'{word},{translation}\n')
    print(f'Было сохранено {len(words)} слов в файл {filename}.')


# Временная проверка
if __name__ == '__main__':
    # Тестируем save_words: создаём словарь и сохраняем его в тестовый файл.
    test_words = {'яблоко': 'apple', 'кошка': 'cat'}
    save_words(test_words, 'test_save.txt')

"""
def print_statistics(score, total_time):
    ...


def ask_and_check(word, correct):
    ...


def start_game(words):
    ...


def train_until_mistake(words):
    ...


def add_words(words):
    ...


def show_all_words(words):
    ...


def main():
    while True:
        menu = '''Меню:
        1. Начать игру
        2. Добавить слова
        3. Тренировка до первой ошибки
        4. Вывод всех слов
        5. Выход
        '''
        print(menu)
        menu_choice = input('Пункт меню: ')


if __name__ == '__main__':
    main()"""
