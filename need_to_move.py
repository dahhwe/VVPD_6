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
