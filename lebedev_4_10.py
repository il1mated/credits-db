"""Практическая работа 4."""

import pickle

def download_data(file_name):
    """
    Функция которая загружает
    информацию из двоичного файла.
    """
    with open(file_name, "rb") as file:
        credits_db = pickle.load(file)

    return credits_db

def find_borrows(credits_db):
    """
    Функция которая
    находит заемщиков
    по ФИО.
    """
    surname = input("Фамилия: ").strip().lower()
    name = input("Имя: ").strip().lower()
    patronymic = input("Отчество: ").strip().lower()
    found = False

    for credit in credits_db:

        initials = credit["initials"]

        if (
            initials["surname"].lower() == surname and
            initials["name"].lower() == name and
            initials["patronymic"].lower() == patronymic
        ):
            print("")

            print("Заемщик найден:",
                surname.title(),
                name.capitalize(),
                patronymic.capitalize()
                )

            print(f"Сумма кредита: {credit["credit_sum"]} рублей.")
            print(f"Срок кредита: {credit["credit_term"]} месяцев.")
            print(f"Кредитная ставка: {credit["percent_rate"]} процентов.")
            print("")

            found = True

    if not found:
        print("Заемщик не найден.")


def long_credits_count(credits_db):
    """
    Функция которая
    находит самые
    длительные кредиты.
    """
    try:
        credits_count = input("Сколько займов вывести: ").strip()

        if not credits_count.isdigit():
            raise ValueError("Нужно ввести целое число.")
        credits_count = int(credits_count)

        print("")

        if credits_count <= 0:
            raise ValueError("Кол-во должно быть больше 0.")

        if credits_count > len(credits_db):
            raise ValueError(f"Заемщиков всего {len(credits_db)}.")

    except ValueError as error:
        print(error)
        return

    longest_credits = sorted(
        credits_db,
        key=lambda credit: credit["credit_term"],
        reverse=True
        )[:credits_count]

    for credit in longest_credits:
        initials = credit["initials"]
        surname = initials["surname"].title()
        name = initials["name"][0].upper()
        patronymic = initials["patronymic"][0].upper()

        print(f"Заемщик: {surname} {name}. {patronymic}.")
        print(f"Длительность кредита: {credit["credit_term"]} мес.")
        print("")

def filter_percent_data(credits_db):
    """
    Функция которая
    фильтрует кредиты
    по процентной ставке.
    """
    percent_rate = float(input("Введите процентную ставку: ").strip())
    count = 0
    print(f"По кредитной ставке {percent_rate}% найдено: \n")

    for credit in credits_db:

        initials = credit["initials"]
        surname = initials["surname"].title()
        name = initials["name"].capitalize()
        patronymic = initials["patronymic"].capitalize()

        if percent_rate == credit["percent_rate"]:

            count += 1
            print(f"{count}) {surname} {name[0]}. {patronymic[0]}.")
            print(f"Долг: {credit["credit_sum"]} рублей.")
            print(f"Срок кредита: {credit["credit_term"]} месяцев.")
            print("")

    if count == 0:
        print("По данной ставке ничего не найдено.")

def add_borrows(credits_db):
    """
    Функция которая
    добавляет заемщиков.
    """
    surname = input("Фамилия: ").strip().lower()
    name = input("Имя: ").strip().lower()
    patronymic = input("Отчество: ").strip().lower()
    credit_sum = float(input("Сумма кредита: ").strip())
    percent_rate = float(input("Процентная ставка: ").strip())
    credit_term = int(input("Срок кредита: ").strip())

    new_borrow = {
        "initials": {
            "surname": surname,
            "name": name,
            "patronymic": patronymic
        },
        "credit_sum": credit_sum,
        "percent_rate": percent_rate,
        "credit_term": credit_term
    }

    credits_db.append(new_borrow)

def delete_borrows(credits_db):
    """
    Функция которая
    удаляет заемщиков.
    """
    surname = input("Фамилия: ").strip().lower()
    name = input("Имя: ").strip().lower()
    patronymic = input("Отчество: ").strip().lower()
    credit_sum = float(input("Сумма кредита: ").strip())
    credit_term = int(input("Срок кредита: ").strip())

    for borrow in credits_db:
        initials = borrow["initials"]
        if (
            initials["surname"].lower() == surname and
            initials["name"].lower() == name and
            initials["patronymic"].lower() == patronymic and
            borrow["credit_sum"] == credit_sum and
            borrow["credit_term"] == credit_term
        ):
            credits_db.remove(borrow)
            print("Заемщик удален.")
            break

    else:
        print("Такого заемщика нет.")

def save_data(credits_db, file_name):
    """
    Функция которая сохраняет
    информацию в двоичный файл.
    """
    with open(file_name, "wb") as file:
        pickle.dump(credits_db, file)

def show_menu_text():
    """
    Функция которая
    показывает 
    текст меню.
    """
    print("------------- Информация о кредитах -------------")
    print("Загрузить информацию из двоичного файла - 1.")
    print("Найти заемщиков по ФИО - 2.")
    print("Вывести количество самых длительных кредитов - 3.")
    print("Фильтровать по процентной ставке - 4.")
    print("Добавить заемщиков - 5.")
    print("Удалить заемщиков - 6.")
    print("Сохранить информацию в двоичный файл - 7.")
    print("Завершить программу - 0.")

def main():
    """
    Основная функция программы
    которая выводит меню.
    """
    credits_db = [
        {
            "initials": {
                "surname": "Тестовый",
                "name": "Тест",
                "patronymic": "Тестович"
            },
            "credit_sum": 123456789.8765,
            "percent_rate": 123.456789,
            "credit_term": 123456789
        }
    ]

    separator = "-------------------------------------------------"
    flag = True

    while flag:
        show_menu_text()

        try:
            print(separator)
            choice = int(input("Введите число от 0 до 7: "))
            print(separator)

            if choice == 1:
                credits_db = download_data("credits.bin")
                print("Данные из файла загружены.")
                print("")

            elif choice == 2:
                find_borrows(credits_db)
                print("")

            elif choice == 3:
                long_credits_count(credits_db)
                print("")

            elif choice == 4:
                filter_percent_data(credits_db)
                print("")

            elif choice == 5:
                add_borrows(credits_db)
                print("Заемщик добавлен.")
                print("")

            elif choice == 6:
                delete_borrows(credits_db)
                print("")

            elif choice == 7:
                save_data(credits_db, "credits.bin")
                print("Скачан файл с данными о кредитах.")
                print("")

            elif choice == 0:
                flag = False
                print("Программа завершена.")
                print(separator)

            else:
                print("Такого числа нет.")
                print("")

        except ValueError:
            print(separator)
            print("Неверное значение.")
            print("")

        except FileNotFoundError:
            print(separator)
            print("Файл не найден.")
            print("")

if __name__ == "__main__":
    main()
