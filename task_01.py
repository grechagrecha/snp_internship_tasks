from string import ascii_lowercase, digits


class Solution:
    def __init__(self):
        self.s = None
        self.rev_s = None

    @staticmethod
    def _format_string(string) -> str:
        """Возвращает строку без знаков препинания и пробелов"""
        char_list = []

        for i in string:
            if i in ascii_lowercase or i in digits:
                char_list.append(i)

        return ''.join(char_list)

    def is_palindrome(self, string) -> bool:
        self.s = str(string).lower()

        if not self.s.isalnum():
            self.s = self._format_string(self.s)

        self.rev_s = self.s[::-1]

        if self.s == self.rev_s:
            return True
        return False
