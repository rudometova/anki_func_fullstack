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


def show_all_words(words):
    pairs = [f'{word} - {translation}' for word, translation in words.items()]
    print('; '.join(pairs))


def add_words(words):
    print(f'Чтобы закончить, введите {STOP_WORD}')
    while True:
        word = input('Введите слово: ').strip()
        if word.lower() == STOP_WORD.lower():
            break
        translation = input('Введите перевод: ').strip()
        if translation.lower() == STOP_WORD.lower():
            break
        words[word] = translation


# Временная проверка — удали после теста.
if __name__ == '__main__':
    # Тестируем add_words
    test_dict = {'дом': 'house'}
    print("До добавления:", test_dict)
    add_words(test_dict)
    print("После добавления:", test_dict)


"""
def print_statistics(score, total_time):
    ...


def ask_and_check(word, correct):
    ...


def start_game(words):
    ...


def train_until_mistake(words):
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
