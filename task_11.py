class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

    def __str__(self):
        return f'name: {self.name}, cal: {self.calories}'

    @property
    def name(self):
        return self._name

    @name.getter
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def calories(self):
        return self._calories

    @calories.getter
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        self._calories = value

    def is_healthy(self):
        return True if self.calories < 200 else False

    def is_delicious(self):
        return True
