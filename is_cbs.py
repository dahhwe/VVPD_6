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

