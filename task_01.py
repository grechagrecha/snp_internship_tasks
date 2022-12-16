from string import ascii_lowercase, digits


def format_string(s: str) -> str:
    """Возвращает строку без знаков препинания и пробелов"""
    char_list = []

    for i in s:
        if i in ascii_lowercase or i in digits:
            char_list.append(i)

    return ''.join(char_list)


def is_palindrome(s) -> bool:
    string = str(s).lower()

    if not string.isalnum():
        string = format_string(string)

    reversed_string = string[::-1]

    if string == reversed_string:
        return True
    return False
