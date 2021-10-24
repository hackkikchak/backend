from transliterate import translit


def string_translit(input_ru_string: str):
    return translit(input_ru_string, reversed=True)
