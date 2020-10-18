from . import helper


class Comparator:

    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2

    def are_equal(self, cinput):
        return helper.get_output(self.path1, cinput) == helper.get_output(self.path2, cinput)
