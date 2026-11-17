# import random
import sys
import time
from typing import Tuple

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


def print_statistics(score: int, total_time: float) -> None:
    print(f'Ваш итоговый счёт: {score}')
    if score > 0:
        average_time = round(total_time / score, 2)
        print(f'Время игры: {round(total_time, 2)} секунд (среднее время: {average_time} сек.)')
    else:
        print(f'Время игры: {round(total_time, 2)} секунд (среднее время: —)')


def ask_and_check(word: str, correct: str) -> Tuple[bool, bool, float]:
    print(f'Ваше слово: {word}')
    start_time = time.time()
    answer = input('Ваш перевод: ').strip()
    end_time = time.time()
    if answer.lower() == STOP_WORD.lower():
        return True, False, 0.0
    is_correct = answer.lower() == correct.lower()
    answer_time = end_time - start_time
    return False, is_correct, answer_time


# Временная проверка — удали после теста.
if __name__ == '__main__':
    # 1. Тестируем print_statistics
    print("--- Тест статистики ---")
    print_statistics(3, 8.75)
    print_statistics(0, 0.0)
    # 2. Тестируем ask_and_check
    print("\n--- Тест ask_and_check ---")
    # Попробуй ввести правильный ответ 'cat', потом неправильный, потом 'СТОП'
    exit_flag, is_correct, ans_time = ask_and_check('кот', 'cat')
    print(f"Результат: выход={exit_flag}, верно={is_correct}, время={round(ans_time, 2)}")


"""
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
