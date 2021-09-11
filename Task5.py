# Создать список (библиотека книг), состоящий из словарей (книги). Словари должны содержать как минимум 5 полей
# (например, номер, название, год издания...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# library = [{"id" : 123456, "title" : "Война и мир", "author" : "Толстой",...} , {...}, {...}, ...]
# Реализовать функции:
# – вывода информации о всех книгах;
# – вывода информации о книге по введенному с клавиатуры номеру;
# – вывода количества книг, старше введённого года;
# – обновлении всей информации о книге по введенному номеру;
# – удалении книги по номеру.
# Провести тестирование функций.

def AllOut(a):
    for i in range(len(a)):
        print("Номер книги: " + str(a[i]["id"]) + " Название книги: " + str(a[i]["title"]) + " Автор: " + str(
            a[i]["author"]) + " Публикация: "
              + str(a[i]["year"]) + " Среднняя оценка: " + str(a[i]["mark"]) + "/10")
    return 0


def FindNumber(a, x):
    t = True
    for i in range(len(a)):
        if a[i]["id"] == x:
            print("Номер книги: " + str(a[i]["id"]) + " Название книги: " + str(a[i]["title"]) + " Автор: " + str(
                a[i]["author"]) + " Публикация: "
                  + str(a[i]["year"]) + " Среднняя оценка: " + str(a[i]["mark"]) + "/10")
            t = False
    if t:
        print("Такой книги не найдено :( ")
    return 0


def FindDate(a, x):
    t = True
    for i in range(len(a)):
        if a[i]["year"] >= x:
            print("Номер книги: " + str(a[i]["id"]) + " Название книги: " + str(a[i]["title"]) + " Автор: " + str(
                a[i]["author"]) + " Публикация: " + str(a[i]["year"]) + " Среднняя оценка: " + str(a[i]["mark"]) + "/10")
            t = False
    if t:
        print("Таких книг не найдено :( ")
    return 0


def Update(v, x, a, b, c, d):
    t = True
    for i in range(len(v)):
        if v[i]["id"] == x:
            v[i].update({"title": a})
            v[i].update({"author": b})
            v[i].update({"year": c})
            v[i].update({"mark": d})
            t = False
    if t:
        print("Такой книги не найдено :( ")
        return 0


def Del(a, x): #Не правильно!!!!!!!!!
    t = True
    for i in range(len(a)):
        if a[i]["id"] == x:
            #a.remove(a[i])
            a[i].clear()
            a[i].update({"id": x})
            a[i].update({"title": "Книга Удалена"})
            a[i].update({"author": "Книга Удалена"})
            a[i].update({"year": "Книга Удалена"})
            a[i].update({"mark" : "Книга Удалена"})
    if t:
        print("Такой книги не найдено :( ")
        return 0


'''def Del(a, x):
    t = True
    i = 0
    while i < len(a):
        if a[i]["id"] == x:
            del a[i]
            t = False
            # i -= 1
        i += 1
    if t:
        print("Такой книги не найдено :( ")
        return 0'''


library = [{"id": 1, "title": "Война и Мир", "author": "Толстой", "year": 1867, "mark": 9},
           {"id": 2, "title": "Потерянный рай", "author": "Мильтон", "year": 1663, "mark": 10},
           {"id": 3, "title": "Властелин колец", "author": "Толкин", "year": 1954, "mark": 6},
           {"id": 4, "title": "Темные начала", "author": "Пулман", "year": 1995, "mark": 7},
           {"id": 5, "title": "Винни Пух", "author": "Милн", "year": 1927, "mark": 3},
           {"id": 6, "title": "Грозовой перевал", "author": "Бронте", "year": 1847, "mark": 8},
           {"id": 7, "title": "Пение птиц", "author": "Фолкс", "year": 1993, "mark": 7},
           {"id": 8, "title": "Унесенные ветром", "author": "Митчелл", "year": 1860, "mark": 5},
           {"id": 9, "title": "Гарри Потер", "author": "Роулинг", "year": 1998, "mark": 4},
           {"id": 10, "title": "Алиса в стране чудес", "author": "Кэррол", "year": 1862, "mark": 6}]
t = True
while t:
    print()
    x = int(input(
        "Выберите действие : \n 1) Вывод информации о всех книгах \n 2) Узнать информацию о книги по номеру \n 3) Вывод всех книг старше введенной даты "
        "\n 4) Обновить информацию о книге по ее номеру \n 5) Удаление книги по номеру \n 6) Для выхода из приложения нажмите 0\n"))
    if x == 1:
        AllOut(library)
    elif x == 2:
        x = int(input("Введите номер книги :"))
        FindNumber(library, x)
    elif x == 3:
        x = int(input("Введите дату публикации от года:"))
        FindDate(library, x)
    elif x == 4:
        x = int(input("Введите номер книги :"))
        a = input("Введите название книги")
        b = input("Введите фамилию автора")
        c = input("Введите год публицации")
        d = input("Введите среднюю оценку")
        Update(library, x, a, b, c, d)
    elif x == 5:
        x = int(input("Введите номер книги :"))
        Del(library, x)
    elif x == 0:
        break
