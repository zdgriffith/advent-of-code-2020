from pathlib import Path
from itertools import product

import numpy as np

floor = 0
empty = 1
occ = 2

def construct_field(fpath):
    field = []
    with fpath.open() as f:
        for r in f.readlines():   
            field.append(np.array([int(i) for i in r.strip().replace(".", str(floor)).replace("L", str(empty))]))
    return np.array(field)


def get_neighbors(idx, field):
    visible_chairs = []
    base = np.array([[1, -1], [1, 0], [1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]])
    for shift in base:
        n_idx = idx + shift
        while True:
            if not ((n_idx[0] >= 0) & (n_idx[0] < field.shape[0])):
                break
            elif not ((n_idx[1] >= 0) & (n_idx[1] < field.shape[1])):
                break
            elif field[tuple(n_idx)] != floor:
                visible_chairs.append(field[tuple(n_idx)])
                break
            else:
                n_idx += shift
    return np.array(visible_chairs)


def cycle(field):
    new_field = np.zeros(field.shape)
    for idx in product(range(field.shape[0]), range(field.shape[1])):
        if field[idx] == floor:
            continue
        neighbors = get_neighbors(idx, field)
        if field[idx] == occ and np.sum(neighbors == occ) >= 5:
            new_field[idx] = empty
        elif field[idx] == empty and np.all(neighbors != occ):
            new_field[idx] = occ
        else:
            new_field[idx] = field[idx]
    return new_field


if __name__ == "__main__":
    field = construct_field(Path(__file__).parent / "input.txt")

    i = 0
    while True:
        i += 1
        print(i)
        new_field = cycle(field)
        if np.all(field == new_field):
            print(np.sum(field == occ))
            break
        else:
            field = new_field