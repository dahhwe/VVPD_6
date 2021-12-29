# Практическая работа №6
ПСП – правильная скобочная последовательность – последовательность из открывающих «(« и закрывающих «)» круглых скобок. Программа содержит две функции:
- Первая функция. Проверяет, является ли полученная строка ПСП.
- Вторая функция. При заключении что строке не ПСП, находит количество изменений, чтобы получить ПСП из полученной строки.

## Оглавление

1. [Функция *is_cbs*](#Функция-is_cbs)
2. [Функция *need_to_move*](#Функция-need_to_move)
3. [Вставка изображения](#Вставка-изображения)

## Функция is_cbs
Функция *is_cbs* проверяет, является ли полученная строка ПСП. При заключении, что полученная строка ПСП функция возвращает 1, в противном случае 0.
Код функции:
```python
def is_cbs(string_to_check: str) -> int:
    """
    Функция проверяет, является ли полученная строка ПСП
    :param string_to_check: Полученная строка
    :return:string_to_check При заключении, что полученная строка ПСП,
     функция возвращает 1, в противном случае 0
    """
    brackets = ['«»', '<>', '()', '{}', '[]']
    while any(x in string_to_check for x in brackets):
        for bracket_parts in brackets:
            string_to_check = string_to_check.replace(bracket_parts, '')
    return not string_to_check
```

## Функция *need_to_move*
Функция *need_to_move* находит количество изменений, необходимых для получения ПСП из полученной строки.
Код функции:
```python
def need_to_move(lisp_reference: str) -> int:
    """
    Функция находит количество изменений,
    чтобы получить ПСП из полученной строки.
    :param lisp_reference:Полученная строка
    :return: количество изменений,
    чтобы получить ПСП из полученной строки
    """
    open_brackets = ['«', '<', '(', '{', '[']
    close_brackets = ['»', '>', ')', '}', ']']
    total = 0
    temp = 0
    for p in lisp_reference:
        if p in open_brackets:
            total += 1
        elif p in close_brackets and total:
            total -= 1
        else:
            temp += 1
    return total + temp
```

## Вставка изображения
Пример вставки изображения:
![Пример изображения](https://i.ibb.co/fQrTFV1/Hc-ARyz52-QXs.jpg, "Minecraft is life")

Для оформления этого файла был использован язык разметки [markdown](https://ru.wikipedia.org/wiki/Markdown).
____
[:arrow_up:Оглавление](#Оглавление)
____
