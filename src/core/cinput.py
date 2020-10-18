class Cinput:

    def __init__(self):
        self.lines = []

    def add_line(self, line):
        self.lines.append(line)
        return self

    def generate(self):
        results = []
        for line in self.lines:
            results.append(line.generate())
        return "\n".join(results)
