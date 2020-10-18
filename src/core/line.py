class Line:

    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)
        return self

    def generate(self):
        results = []
        for entry in self.entries:
            results.append(entry.generate())
        return " ".join(results)
