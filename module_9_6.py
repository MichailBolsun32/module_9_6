#Напишите функцию-генератор all_variants(text),
# которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.


def all_variants(text):
    for length in range(1, len(text) + 1):  # итерация по всем возможным длинам подстрок
        for index_start in range(len(text) - length + 1):  # итерация для выборки подстроки
           yield text[index_start:index_start + length]  # Возвращаем подстроку



a = all_variants("abc")
for i in a:
    print(i)

