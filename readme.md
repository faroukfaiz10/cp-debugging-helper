# Competitive programming debugging helper

This is a program that can help you debug your code, especially in competitive programming contests where time is of the essence. It basically generates random inputs according to rules you can specify, and compares your code's output with output's of a known working solution[^1].

- Only numbers(integers) are supported for now
- Only python scripts are supported for now

## Input

The **input** (`Cinput`) is composed of **lines** (`Line`) . Each line can contain multible **numbers**(`Number`).
The **inclusive** lower and upper bound should be specified to the `Number` constructor.
`Line` (resp. `CInput`) has a method `add_number` (resp. `add_line`) to add a number (resp. line).

## How it works (Example)

The _main.py_ file is the only one to be modified. Combined with the files at the test directory, it illustrates a working example of an input of the following format:

```
a b
c
```

Where **_a_** belongs to segment **_[1, 10]_**, **_b_** to the segment **_[1, 20]_** and **_c_** to the segment **_[1, 15]_**
The files **_file1_** and **_file2_** are similar except for the case where `a == b == c`.
Running the _main.py_ file will generate at most `MAX_ITER` inputs. As soon as one of them gives different outputs on the two scripts (_file1_ and _file2_), it is displayed and the program finishes. If no input is found, a message _Could not find a suitable input_ is displayed instead. In this case, it will either print 3 equal numbers (e.g. _3 3 3_)[^2] or print _Could not find a suitable input_ message.

## How to use

Modify the input to suit your problem (see input and example above), then the path to your python scripts (the one that has a correct solution [^1], and the one to debug of course). You can modify the `MAX_ITER` if you want. Try to keep the numbers ranges small if no solution is found after a long time

[^1]: One such program can usually be implemented very fast without taking time constraints. Or if not in a live contest, any accepted script (written by someone else) will do the work.
[^2]: Most likely case given how small the number ranges are (i.e. at most a length of 20 for 3 numbers) compared to `MAX_ITER`
