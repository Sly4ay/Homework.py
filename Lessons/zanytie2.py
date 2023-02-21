string_sample1 = "Hello world world"
                # 0123456789
string_sample2 = "first letteR is lowErcase.How are you"
string_sample3 = "            extra whitespace string    ** * * *      "
german_sample = "der Fluß"

# есть индексация в пайтоне [] в после слова и в скобках указывается индекс
# какую букву хотите взять print(string_sample1[1]) в примере выйдет буква 'E'
# отчётность идёт с цифры 0 1 2 3 4 5 6 7 8 9
# можно ствить отрицательное значение [-1] выдаст символ с конца
# отчётноcть идёт -1 -2 -3 -4 -5 -6

# можно брать диапазон [6:11] [START:END] [START : ] от старта до конца предложения
# [START:END:STEP] есть ещё параметр шаг  : : 2 это будет каждый второй символ
print(string_sample1[-1])
print(string_sample1[6:11])
print(string_sample1[::2])

# c шагом -1 это значит в обратном порядке

print(string_sample1[::-1])

# len вызывает длинну строки
print(string_sample1[len(string_sample1) - 1])

print(string_sample1.upper())
string_sample1 = string_sample1.upper()


print(german_sample.lower())
print(german_sample.casefold())

print(string_sample1.isupper()) # проверяет что вся строка в верхнем регистре
print(string_sample1.islower()) # проверяет что вся строка в нижнем регистре

print(string_sample2.capitalize()) # делает первую букву заглавной а остальные в нижнем регстри
print(string_sample2.title()) # делает первую букву слова с заглавной буквы

print(string_sample3.strip('* ')) # удалить все лишние пробелы в начале и в конце строки(только края)
                              # можно указать условия которые удаляются в скобках(*  )
print(string_sample3.lstrip('* ')) # Удаляет слева
print(string_sample3.rstrip('* ')) # Удаляет справа

# r сырая строка
# f форматированная строка

print(string_sample1.replace('world', 'planet'))  # меняет слова. нужно два аргумента. первый слово которое меняем
                                                  # второе слово на которое меняем


print(string_sample1.split())                            # создаёт массив

# a, b, c = string_sample1.split()
# print(a)
# print(b)
# print(c)

print(string_sample1.count('WORLD'))           # считает количество символов или слов
print(string_sample1.find('WORLD'))            # находит первое сопадение в предложении

print('WORLD' in string_sample1)               # проверяет находится ли это слово в строке

