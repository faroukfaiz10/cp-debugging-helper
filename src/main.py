from core.cinput import Cinput
from core.line import Line
from core.number import Number
from core.comparator import Comparator

from os import getcwd, path

MAX_ITER = 5000

# Define input
cinput = Cinput()
cinput.add_line(
    Line()
    .add_entry(Number(1, 10))
    .add_entry(Number(1, 20))
).add_line(
    Line()
    .add_entry(Number(1, 15))
)

# Define output comparator
dir_path = getcwd()
comparator = Comparator(path.join(dir_path, "test/file1.py"),
                        path.join(dir_path, "test/file2.py"))

# Search for input
iteration = 0
input_found = False
while(not input_found and iteration < MAX_ITER):
    stdin = cinput.generate()
    if not comparator.are_equal(stdin):
        print(stdin)
        input_found = True
    iteration += 1

if not(input_found):
    print("Could not find a suitable input")
