from pathlib import Path

import numpy as np


def construct_field(fpath):
    field = []
    with fpath.open() as f:
        for r in f.readlines():   
            field.append(np.array([int(i) for i in r.strip().replace(".", "0").replace("#", "1")]))
    return np.array(field)


def count_trees(field, right, down):
    trees = 0
    for i, x in enumerate(field[::down]):
        j = right * i
        while j >= len(x):
            j -= len(x)
        if i != 0:
            trees += x[j]
    return trees

if __name__ == "__main__":
    fpath = Path(__file__).parent / "input.txt"
    field = construct_field(fpath)
    print(count_trees(field, 3, 1))

