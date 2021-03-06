from pathlib import Path

import numpy as np

from one import construct_field, count_trees

if __name__ == "__main__":
    paths = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    fpath = Path(__file__).parent / "input.txt"
    field = construct_field(fpath)
    trees = np.zeros(len(paths), dtype=int)
    for i, (right, down) in enumerate(paths):
        trees[i] = count_trees(field, right, down)
    print(trees.prod())

