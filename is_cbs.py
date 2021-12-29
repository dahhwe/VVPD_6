def is_cbs(string_to_check: str) -> int:
    brackets = ['«»', '<>', '()', '{}', '[]']
    while any(x in string_to_check for x in brackets):
        for bracket_parts in brackets:
            string_to_check = string_to_check.replace(bracket_parts, '')
    return not string_to_check

