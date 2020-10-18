from random import randint


class Number:

    def __init__(self, a, b):
        self.lower_bound = a
        self.upper_bound = b

    def generate(self):
        return str(randint(self.lower_bound, self.upper_bound))
