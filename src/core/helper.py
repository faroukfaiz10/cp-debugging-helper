import subprocess


def get_output(path, cinput):
    return subprocess.run(["python3", path], input=cinput, text=True, capture_output=True).stdout
