from vvpd_5 import is_cbs, need_to_move


def main():
    while not (string_to_check := input("Введите строку:")):
        print("Некорректный ввод!")

    if is_cbs.is_cbs(string_to_check):
        print(f"{string_to_check} – правильная скобочная последовательность.")
    else:
        number_of_corrections = need_to_move.need_to_move(string_to_check)
        print(f"{string_to_check} – неправильная скобочная "
              f"последовательность.\n"
              f"строка может стать правильной скобочной последовательностью\n"
              f"после {number_of_corrections} колличества изменений.")


if __name__ == "__main__":
    main()
