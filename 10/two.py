from itertools import combinations
from pathlib import Path

import numpy as np


def valid_combinations(values):
    """ Calculate the total number of combinations for a sequence of adapters,
    where no link in the sequence has a >3 jolt difference.
    """
    total = 0
    for length in range(len(values) - 1):
        total += np.sum(
            np.all(
                np.diff([
                    (values[0], *i, values[-1]) for i in combinations(values[1:-1], length)
                ]) <= 3,
                axis=1,
            )
        )
    return total


if __name__ == "__main__":  
    data = np.sort(np.loadtxt(Path(__file__).parent / "input.txt", dtype=int))
    # add outlet (start) and device(end)
    data = np.array([0] + list(data) + [3 + data.max()])

    # adapters 3 jolts different than a neighbor must always exist
    required = np.argwhere(np.append([True], np.diff(data) == 3)).T[0]

    # split adapters into sequences between required adapters.
    # in these sequences, some can be dropped
    combos = []
    for i in range(len(required) - 1):
        if required[i + 1] - required[i] < 3:
            continue
        combos.append(data[required[i]:required[i + 1]])

    # get the total number of valid combinations for each sub-sequence,
    # then multiply together to find the number of combos for the whole chain.
    total = 1
    for values in combos:
        total *= valid_combinations(values)
    print(total)
