# Импорт библиотеки random
import random


# Функция для перемешки букв в словах
def shuffle_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    shuffled_word = ''.join(word_list)
    return shuffled_word

# Создание переменных для сохранения имени пользвателя и подсчета очков
name_user = input("Введите Ваше имя:\n")
count_point = 0

# Считывается файл со словами
with open('words.txt', 'r', encoding='utf-8') as word_reading:
    while True:
        readble_word = word_reading.readline().rstrip('\n') # создается переменная, в которую сохраняется результат считывания строки
        if not readble_word: # если строка пустая - цикл прерывается
            break
        else: # иначе, вызывается функция
            word_for_user = shuffle_word(readble_word)
            answer = input(f"Угадайте слово: {word_for_user}\n").lower()
            if answer == readble_word: # если ответ совпадает - счетчик баллов увеличивается
                print("Верно! Вы получаете 10 очков!")
                count_point += 10
            else: # иначе - правильный ответ выводится в консоль
                print(f"Неверно! Верный ответ - {readble_word}")

# Запись в файл имени пользователя и количества очков
with open('history.txt', mode='a', encoding="utf-8") as file:
    file.write(f"{name_user} - {count_point} очков\n")

# Запись количества сыгранных игр
with open('history.txt', mode='r', encoding="utf-8") as file:
    print(f"\nВсего игр сыграно: {len(file.readlines())}")

# Запись максимального рекорда
with open('records.txt', 'a', encoding='utf--8') as record:
    record.write(f"{count_point}\n")

list_records = []
for i in open('records.txt'):
    list_records.append(i[:-1])

best_record = max(list_records)

print(f"Максимальный рекорд: {best_record}")
