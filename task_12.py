from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self._flavor = flavor

    def __str__(self):
        return f'name: {self.name}, cal: {self.calories}, flavor: {self.flavor}'

    @property
    def flavor(self):
        return self._flavor

    @flavor.getter
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        self._flavor = flavor

    def is_delicious(self):
        return False if self.flavor == 'black licorice' else True
    