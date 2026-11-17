import random
import sys
import time
from typing import Tuple

STOP_WORD = 'СТОП'


def load_words(filename="words.txt"):
    """
    Загружает пары «слово, перевод» из файла и возвращает словарь.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            words = {}
            for line in file:
                line = line.strip()
                if ',' in line:
                    parts = line.split(',')
                    if len(parts) == 2:
                        word = parts[0].strip()
                        translation = parts[1].strip()
                        if word and translation:
                            words[word] = translation
            return words
    except FileNotFoundError:
        print(f'Ошибка: файл {filename} не найден.')
        sys.exit(1)


def save_words(words, filename="words.txt"):
    """
    Сохраняет словарь в файл в формате «слово,перевод» построчно.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for word, translation in words.items():
            file.write(f'{word},{translation}\n')
    print(f'Было сохранено {len(words)} слов в файл {filename}.')


def show_all_words(words):
    """
    Выводит все пары «слово - перевод» в одну строку через '; '.
    """
    pairs = [f'{word} - {translation}' for word, translation in words.items()]
    print('; '.join(pairs))


def add_words(words):
    """
    Добавляет новые пары «слово, перевод» в словарь по запросу пользователя.
    """
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
    """
    Выводит итоговую статистику игры: счёт, общее время и среднее время.
    """
    print(f'Ваш итоговый счет: {score}')

    # Форматируем общее время: всегда 2 знака после запятой
    formatted_total = f'{total_time:.2f}'

    if score > 0:
        average_time = total_time / score
        formatted_avg = f'{average_time:.2f}'
        print(
            f'Время игры: {formatted_total} секунд '
            f'(среднее время: {formatted_avg} сек.)'
        )
    else:
        print(
            f'Время игры: {formatted_total} секунд '
            f'(среднее время: —)'
        )


def ask_and_check(word: str, correct: str) -> Tuple[bool, bool, float]:
    """
    Спрашивает перевод слова. Возвращает (флаг выхода, правильность, время).
    """
    print(f'Ваше слово: {word}')
    start_time = time.time()
    answer = input('Ваш перевод: ').strip()
    end_time = time.time()

    if answer.lower() == STOP_WORD.lower():
        return True, False, 0.0

    is_correct = answer.lower() == correct.lower()
    answer_time = end_time - start_time
    return False, is_correct, answer_time


def start_game(words):
    """
    Запускает обычный игровой режим с подсчётом очков и времени.
    """
    if not words:
        print('Словарь пуст. Добавьте слова для игры.')
        return

    print(f'Чтобы закончить, введите {STOP_WORD}')
    score = 0
    total_time = 0.0
    words_list = list(words.keys())

    while True:
        word = random.choice(words_list)
        correct = words[word]

        exit_flag, is_correct, answer_time = ask_and_check(word, correct)

        if exit_flag:
            break

        total_time += answer_time

        if is_correct:
            score += 1
            print(f'Верно! Время на ответ: {round(answer_time, 2)} секунд')
        else:
            print(
                f'Неправильно, правильный ответ: {correct} '
                f'(Время на ответ: {round(answer_time, 2)} секунд)'
            )

    print('Спасибо за игру!')
    print_statistics(score, total_time)


def train_until_mistake(words):
    """
    Режим «до первой ошибки»: игра завершается после первой ошибки или СТОП.
    """
    if not words:
        print('Словарь пуст. Добавьте слова для игры.')
        return

    print('Режим: Игра до первой ошибки! Чтобы выйти вручную, введите СТОП')
    score = 0
    total_time = 0.0
    words_list = list(words.keys())

    while True:
        word = random.choice(words_list)
        correct = words[word]

        exit_flag, is_correct, answer_time = ask_and_check(word, correct)

        if exit_flag:
            print('Выход из режима по запросу пользователя.')
            break

        total_time += answer_time

        if is_correct:
            score += 1
            print(
                f'Верно! Всего очков: {score} '
                f'(ответ за {round(answer_time, 2)} секунд)'
            )
        else:
            print(f'Ошибка! Неверно. Правильный ответ: {correct}')
            break

    print_statistics(score, total_time)


def main():
    """
    Главное меню программы.
    """
    words = load_words()
    print(f'Было загружено {len(words)} слов из файла words.txt')

    while True:
        menu = '''Меню:
    1. Начать игру
    2. Добавить слова
    3. Тренировка до первой ошибки
    4. Вывод всех слов
    5. Выход
    '''
        print(menu)
        menu_choice = input('Пункт меню: ').strip()

        if menu_choice == '1':
            start_game(words)
        elif menu_choice == '2':
            add_words(words)
        elif menu_choice == '3':
            train_until_mistake(words)
        elif menu_choice == '4':
            show_all_words(words)
        elif menu_choice == '5':
            save_words(words)
            sys.exit()
        else:
            print('Неизвестный пункт меню')


if __name__ == '__main__':
    main()
